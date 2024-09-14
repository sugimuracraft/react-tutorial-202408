from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from core.settings import AppSettings
from core.constants import SERVERS

app = FastAPI()
app.openapi_schema = None

app_settings = AppSettings()

# CORS settings.
# see: https://fastapi.tiangolo.com/ja/tutorial/cors/#corsmiddleware
cors_origins = [app_settings.front_endpoint]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# OpenAPI settings.
# see: https://fastapi.tiangolo.com/ja/how-to/extending-openapi/?h=get_openapi#overriding-the-defaults
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="App API",
        version="1.0.0",
        description="学習時間を記録できるアプリです。",
        routes=app.routes,
    )
    openapi_schema["servers"] = SERVERS
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
