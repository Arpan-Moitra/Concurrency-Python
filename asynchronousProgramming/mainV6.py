import asyncio


async def async_sleep(seconds):
    await asyncio.sleep(seconds)
    return seconds


async def main():
    pending = set()
    for i in range(1, 11):
        pending.add(asyncio.create_task(async_sleep(i)))

    add_task = True

    while len(pending) > 0:
        done, pending = await asyncio.wait(pending, return_when='FIRST_COMPLETED')
        # done, pending = await asyncio.wait(pending, timeout=2)

        print("DONE:")
        for done_task in done:
            print(await done_task)

        if add_task:
            pending.add(asyncio.create_task(async_sleep(1)))
            add_task = False


if __name__ == "__main__":
    asyncio.run(main())
