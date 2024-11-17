from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from fastapi.responses import FileResponse, ORJSONResponse

from .api import router as api_router


app = FastAPI(
    default_response_class=ORJSONResponse,
    docs_url=None,
    redoc_url=None,
)
app.include_router(api_router)


@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,  # type: ignore
        title=app.title + ' - Swagger UI',
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url='/swagger-js',
        swagger_css_url='/swagger-css',
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)  # type: ignore
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get('/swagger-css')
def get_swagger_css():
    return FileResponse('./static/swagger/swagger-ui.css')


@app.get('/swagger-js')
def get_swagger_js():
    return FileResponse('./static/swagger/swagger-ui-bundle.js')
