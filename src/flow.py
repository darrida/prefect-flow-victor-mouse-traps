from pprint import pprint

from prefect import flow, task
from prefect.blocks.system import Secret
from victor_mouse_trap import VictorApi, VictorAsyncClient


@flow(name="victor-trap-status")
async def main():
    username = Secret.load("victor_username")
    password = Secret.load("victor_password")

    async with VictorAsyncClient(username.get(), password.get()) as client:
        api = VictorApi(client)
        traps = await api.get_traps()
        for t in traps:
            pprint(t.model_dump())
            pprint(t.trapstatistics.model_dump())
        # return
        # d = await api.get_trap_history(trap_id=143485)
        # for x in d:
        #     print(x.time_stamp, x.activity_type_text)
    