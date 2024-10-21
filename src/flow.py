import asyncio
from datetime import datetime

from prefect import flow, get_run_logger, pause_flow_run, suspend_flow_run
from prefect.blocks.system import Secret
from zoneinfo import ZoneInfo

from victor_mouse_trap import VictorApi, VictorAsyncClient
from victor_mouse_trap._models import TrapStatistics


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
            if trap.trapstatistics.kills_present == 1:
                last_date = local_time(trap.trapstatistics.last_kill_date)
                logger.error(f"{trap.name} | TRIPPED | When Tripped: {last_date} (24hr) | battery: {trap.trapstatistics.battery_level}")
                trapped = True
            else:
                last_date = local_time(trap.trapstatistics.last_report_date)
                logger.info(f"{trap.name} | CLEAR | Last Checked: {last_date} (24hr) | battery: {trap.trapstatistics.battery_level}")

        if trapped is True:
            await pause_flow_run(timeout=20_000)
            logger.info("CAUGHT MOUSE.")
        else:
            logger.info("No mice this time...")


def local_time(datetime_: datetime, output_format: str = "%H:%M", tz: str = "America/Chicago") -> str:
    # datetime_ = datetime.strptime(timestamp, str_format)
    datetime_ = datetime_.astimezone(ZoneInfo(tz))
    return datetime_.strftime(output_format)

if __name__ == "__main__":
    asyncio.run(main())