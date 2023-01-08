import asyncio

async def main():
    print('Hello')
    await foo('Text')
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

