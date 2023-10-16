import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("func 1")
    return "rahul"

async def main():
    result = await function1()
    print(result)