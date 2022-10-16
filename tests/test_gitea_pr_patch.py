from pr_size_control.gitea_pr_patch import GiteaPRPatch


async def test():
    got = await GiteaPRPatch('link').value()

    assert got == 'lol'
