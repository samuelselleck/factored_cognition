from ice.recipe import recipe


async def say_hello():
    _ = other()
    _ = await other_async()
    return "Hello world!"


def other():
    return "this is returned from other"


async def other_async():
    return "this is returned from other async"

recipe.main(say_hello)
