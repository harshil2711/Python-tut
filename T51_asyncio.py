import asyncio
import time


async def funtion1():
    # await asyncio.sleep(3)
    print("function 1")

async def funtion2():
    # await asyncio.sleep(3)
    print("function 2")

async def funtion3():
    # await asyncio.sleep(3)
    print("function 3")


#
# funtion1()
# funtion2()
# funtion3()

async def main():
    L = await asyncio.gather(
    funtion1(),
    funtion2(),
    funtion3(),
    )


