class TokenGranter:
    def __init__(self, token_granter_url: str) -> None: ...
    def grant_access_token(
        self, username: str, password: str, temporary: bool
    ) -> str: ...
    def validate_token(self, username: str, token: str) -> bool: ...
