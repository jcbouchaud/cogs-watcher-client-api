from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.oauth import router as oauth_router


app = FastAPI()

app.include_router(oauth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#     user_oauth = OAuth1Session(CONSUMER_KEY,
#                           client_secret=CONSUMER_SECRET,
#                           resource_owner_key=user_key,
#                           resource_owner_secret=user_secret,
#                           )
#     identity_response = user_oauth.get("https://api.discogs.com/oauth/identity")
#     username = identity_response.json()["username"]
#     return AuthenticateResponse(user_key=user_key, user_secret=user_secret, username=username)
