import asyncio
from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from .crud import query_SongCi_by_like_paginated, query_QuanTangShi_by_like_paginated
from .database import engine, get_db
from .dump2sqlite import fill_sqlite
from .models import *
from .schemas import ReadSongCi, ReadQuanTangShi

# 配置 json 文件夹路径 "./third-repository/chinese-poetry"
root_path = None


# 子应用的 lifespan
@asynccontextmanager
async def culture_lifespan(app: APIRouter):
    # 启动后台任务，不阻塞启动流程
    await asyncio.create_task(fill_sqlite(root_path))
    yield
    # print("子应用即将关闭...")


app = APIRouter(lifespan=culture_lifespan)
templates = Jinja2Templates(directory='./culture/templates')

Base.metadata.create_all(bind=engine)


# @app.get("/SongCi/{word}", response_model=list[ReadSongCi])
# def read_items(word: str, db: Session = Depends(get_db)):
#     items = query_SongCi_by_like(db, word)
#     return items


# # 处理查询并渲染模板
# @app.get("/SongCi/{word}", response_class=HTMLResponse)
# async def read_items(request: Request, word: str, db: Session = Depends(get_db)):
#     # 查询数据
#     songci_list = query_SongCi_by_like(db, word)
#     # 使用 from_orm 将查询结果转换为 Pydantic 模型列表
#     items = [ReadSongCi.model_validate(songci) for songci in songci_list]
#     # 渲染模板并传递查询结果
#     return templates.TemplateResponse("song_ci_template.html", {"request": request, "word": word, "items": items})


# 查询并渲染分页数据
@app.get("/SongCi/{word}", response_class=HTMLResponse)
async def read_items(request: Request, word: str, page: int = 1, db: Session = Depends(get_db)):
    # 每页显示的条目数
    items_per_page = 10
    # 计算跳过的条目数 (skip)
    skip = (page - 1) * items_per_page
    # 查询分页数据
    songci_list = query_SongCi_by_like_paginated(db, word, skip, items_per_page)
    # 获取总条目数
    total_count = db.query(func.count(SongCi.id)).filter(SongCi.paragraphs.like(f"%{word}%")).scalar()
    # 转换为 Pydantic 模型
    items = [ReadSongCi.model_validate(songci) for songci in songci_list]
    # 计算总页数
    total_pages = (total_count + items_per_page - 1) // items_per_page
    # 渲染模板并传递数据
    return templates.TemplateResponse("song_ci_template.html", {
        "request": request,
        "word": word,
        "items": items,
        "current_page": page,
        "total_pages": total_pages,
    })


@app.get("/QuanTangShi/{word}", response_class=HTMLResponse)
async def read_items(request: Request, word: str, page: int = 1, db: Session = Depends(get_db)):
    # 每页显示的条目数
    items_per_page = 10
    # 计算跳过的条目数 (skip)
    skip = (page - 1) * items_per_page
    # 查询分页数据
    quan_tang_shi = query_QuanTangShi_by_like_paginated(db, word, skip, items_per_page)
    # 获取总条目数
    total_count = db.query(func.count(QuanTangShi.id)).filter(QuanTangShi.paragraphs.like(f"%{word}%")).scalar()
    # 转换为 Pydantic 模型
    items = [ReadQuanTangShi.model_validate(quantangshi) for quantangshi in quan_tang_shi]
    # 计算总页数
    total_pages = (total_count + items_per_page - 1) // items_per_page
    # 渲染模板并传递数据
    return templates.TemplateResponse("quan_tang_shi_template.html", {
        "request": request,
        "word": word,
        "items": items,
        "current_page": page,
        "total_pages": total_pages,
    })
