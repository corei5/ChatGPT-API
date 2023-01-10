import os
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from common.errors import OrkgNlpApiError
from common.util import io

from routers import ChatGPT

_registered_services = []


def create_app():
    app = FastAPI(
        title='ChatGPT API',
        root_path=os.getenv('ChatGPT_API', ''),
        servers=[
            {'url': os.getenv('ChatGPT_API', ''), 'description': ''}
        ],
    )

    _configure_app_routes(app)
    _configure_exception_handlers(app)
    _configure_cors_policy(app)
    _save_openapi_specification(app)

    return app


def _configure_app_routes(app):
    app.include_router(ChatGPT.router)

def _configure_exception_handlers(app):
    pass


def _configure_cors_policy(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False
    )


def _save_openapi_specification(app):
    app_dir = os.path.dirname(os.path.realpath(__file__))
    io.write_json(app.openapi(), os.path.join(app_dir, '..', 'openapi.json'))
