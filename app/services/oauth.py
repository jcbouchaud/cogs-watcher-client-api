from typing import Annotated
from fastapi import Header
from requests import Session
from requests_oauthlib import OAuth1Session
from app.config import settings


class CogsClient:
    _request_token_url = f"https://api.discogs.com/oauth/request_token"
    _authorization_url = f"https://discogs.com/oauth/authorize"
    _access_token_url = "https://api.discogs.com/oauth/access_token"
    _identity_url = "https://api.discogs.com/oauth/identity"

    def __init__(self, session: Session):
        self.session: Session = session

    def request_token(self) -> str:
        return self.session.fetch_request_token(self._request_token_url)

    def get_authorization_url(self) -> str:
        return self.session.authorization_url(self._authorization_url)

    def fetch_access_token(self) -> str:
        return self.session.fetch_access_token(self._access_token_url)

    def get_identity(self):
        return self.session.get(self._identity_url)


def get_oauth_session(
        oauth_token: Annotated[str | None, Header()] = None,
        oauth_token_secret: Annotated[str | None, Header()] = None,
        verifier: Annotated[str | None, Header()] = None,
        callback_uri: Annotated[str | None, Header()] = None
):
    session_params = {
        "client_key": settings.CONSUMER_KEY,
        "client_secret": settings.CONSUMER_SECRET
    }

    if oauth_token:
        session_params["resource_owner_key"] = oauth_token

    if oauth_token_secret:
        session_params["resource_owner_secret"] = oauth_token_secret

    if verifier:
        session_params["verifier"] = verifier

    if callback_uri:
        session_params["callback_uri"] = callback_uri

    session = OAuth1Session(**session_params)

    try:
        yield session

    finally:
        session.close()
