import asyncio

from prefect import flow, get_run_logger, pause_flow_run
from prefect.blocks.system import Secret

from victor_mouse_trap import VictorApi, VictorAsyncClient


@flow(name="victor-trap-status")
async def main():
    logger = get_run_logger()

    username: Secret = await Secret.load("victor-username")
    password: Secret = await Secret.load("victor-password")

    async with VictorAsyncClient(username.get(), password.get()) as client:
        api = VictorApi(client)
        traps = await api.get_traps()

        trapped = False
        for trap in traps:
            if trap.trapstatistics.kills_present == 0:
                logger.error(f"{trap.name} | TRIPPED | When Tripped: {trap.trapstatistics.last_kill_date}")
                trapped = True
            else:
                logger.info(f"{trap.name} | CLEAR | Last Checked: {trap.trapstatistics.last_report_date}")

        if trapped is True:
            string = await pause_flow_run(wait_for_input=str, timeout=21_600)
            logger.info(f"Some thing... {string}")
        else:
            logger.info("No mice this time...")
            

if __name__ == "__main__":
    asyncio.run(main())