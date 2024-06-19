from token_granter_wrapper import token_granter


def test_token_granter():
    tk = token_granter.TokenGranter("here")
    assert "" == tk.grant_access_token("TEST", "TEST", False)
