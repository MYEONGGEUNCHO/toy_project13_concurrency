import asyncio




async def main():
    async with asyncio.timeout(10):
        await long_running_task()