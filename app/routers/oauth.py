from typing import Annotated
from fastapi import APIRouter, Depends, Header
from requests import Session
from app.services.oauth import CogsClient, get_oauth_session
from app.schemas.oauth import AuthorizationResponse, OauthTokens


router = APIRouter(tags=["oauth"], prefix="/auth")


@router.get("/authorize-oauth", response_model=AuthorizationResponse)
def authorize_oauth(
        callback_uri: Annotated[str | None, Header()] = None,
        session: Session = Depends(get_oauth_session),
):
    client = CogsClient(session)
    tokens = client.request_token()

    return AuthorizationResponse(
        oauth_token=tokens.get('oauth_token'),
        oauth_token_secret=tokens.get('oauth_token_secret'),
        authorization_url=client.get_authorization_url()
    )


@router.get("/authenticate", response_model=OauthTokens)
async def authenticate(
        oauth_token: Annotated[str | None, Header()] = None,
        oauth_token_secret: Annotated[str | None, Header()] = None,
        verifier: Annotated[str | None, Header()] = None,
        session: Session = Depends(get_oauth_session)
):
    client = CogsClient(session)
    tokens = client.fetch_access_token()

    return OauthTokens(
        oauth_token=tokens.get('oauth_token'),
        oauth_token_secret=tokens.get('oauth_token_secret')
    )

@router.get("/identity")
async def get_identity(
        oauth_token: Annotated[str | None, Header()] = None,
        oauth_token_secret: Annotated[str | None, Header()] = None,
        session: Session = Depends(get_oauth_session)
):
    client = CogsClient(session)
    res = client.get_identity()
    return res.json()