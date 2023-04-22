from app.schemas.utils import CamelBaseModel


class OauthTokens(CamelBaseModel):
    oauth_token: str
    oauth_token_secret: str


class AuthorizationResponse(OauthTokens):
    authorization_url: str
