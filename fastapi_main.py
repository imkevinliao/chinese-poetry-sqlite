import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from culture import app as culture_app

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# 允许多个来源
origins = [
    "http://localhost",  # 本地开发环境
    "http://localhost:3000",  # 前端开发环境
    "http://127.0.0.1",  # 本地 IP 地址
    # "https://example.com",  # 生产环境的一个域名
    # "https://sub.example.com",  # 子域名
    # "https://*.example.com",  # 允许 example.com 域名下的所有子域
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的跨域来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

app.include_router(culture_app, prefix='/culture', tags=['culture(tag)'])

templates = Jinja2Templates(directory="./templates")


@app.get("/", response_class=HTMLResponse)
async def hello_world(request: Request):
    full_url = str(request.url)
    return templates.TemplateResponse("index.html", {"request": request, "url": full_url})


if __name__ == '__main__':
    uvicorn.run("fastapi_main:app", host='0.0.0.0', port=8000, reload=False)
