from typing import List

from sqlalchemy.orm import Session

from . import schemas, models


def create_WuDaiShiCiHuaJian(db: Session, data: schemas.CreateWuDaiShiCiHuaJian):
    # 通过 paragraphs 查找是否已存在相同的数据
    existing_data = db.query(models.WuDaiShiCiHuaJian).filter_by(paragraphs=data.paragraphs).first()
    if existing_data:
        return existing_data
    db_data = models.WuDaiShiCiHuaJian(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_YuanQu(db: Session, data: schemas.CreateYuanQu):
    existing_data = db.query(models.YuanQu).filter_by(paragraphs=data.paragraphs).first()
    if existing_data:
        return existing_data
    db_data = models.YuanQu(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_QuanTangShi(db: Session, data: schemas.CreateQuanTangShi, ignore_query=False):
    # 全唐诗太多了，每次插入都进行查询会很慢
    if not ignore_query:
        existing_data = db.query(models.QuanTangShi).filter_by(paragraphs=data.paragraphs_origin).first()
        if existing_data:
            return existing_data
    db_data = models.QuanTangShi(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_QuanTangShi_batch(db: Session, data_list: List[schemas.CreateQuanTangShi], ignore_query=False):
    # 如果不需要跳过查询，检查每条数据是否已存在
    if not ignore_query:
        # 创建一个包含所有 paragraphs_origin 的查询条件，避免每次都查询数据库
        paragraphs_origin_list = [data.paragraphs_origin for data in data_list]
        existing_data = db.query(models.QuanTangShi).filter(
            models.QuanTangShi.paragraphs_origin.in_(paragraphs_origin_list)).all()
        # 将查询结果转成字典，方便后续判断
        existing_paragraphs = {item.paragraphs_origin for item in existing_data}
        
        # 过滤出不重复的记录
        data_list = [data for data in data_list if data.paragraphs_origin not in existing_paragraphs]
    
    # 创建模型实例
    db_data = [models.QuanTangShi(**data.model_dump()) for data in data_list]
    
    # 批量插入数据
    db.bulk_save_objects(db_data)
    db.commit()
    
    return db_data


def create_SongCi(db: Session, data: schemas.CreateSongCi):
    existing_data = db.query(models.SongCi).filter_by(paragraphs=data.paragraphs).first()
    if existing_data:
        return existing_data
    db_data = models.SongCi(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_ChuCi(db: Session, data: schemas.CreateChuCi):
    existing_data = db.query(models.ChuCi).filter_by(content=data.content).first()
    if existing_data:
        return existing_data
    db_data = models.ChuCi(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_LunYu(db: Session, data: schemas.CreateLunYu):
    existing_data = db.query(models.LunYu).filter_by(paragraphs=data.paragraphs).first()
    if existing_data:
        return existing_data
    db_data = models.LunYu(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_ShiJing(db: Session, data: schemas.CreateShiJing):
    existing_data = db.query(models.ShiJing).filter_by(content=data.content).first()
    if existing_data:
        return existing_data
    db_data = models.ShiJing(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def query_SongCi_by_like(db: Session, word):
    if not word.startswith('%'):
        word = f'%{word}'
    if not word.endswith('%'):
        word = f'{word}%'
    datas = db.query(models.SongCi).filter(models.SongCi.paragraphs.like(word)).all()
    return datas


def query_SongCi_by_like_paginated(db: Session, word: str, skip: int, limit: int):
    # 使用 SQLAlchemy 的 limit 和 offset 实现分页
    return db.query(models.SongCi).filter(models.SongCi.paragraphs.like(f"%{word}%")).offset(skip).limit(limit).all()


def query_QuanTangShi_by_like_paginated(db: Session, word: str, skip: int, limit: int):
    # 使用 SQLAlchemy 的 limit 和 offset 实现分页
    return db.query(models.QuanTangShi).filter(models.QuanTangShi.paragraphs.like(f"%{word}%")).offset(skip).limit(limit).all()


# common
def count_records(db: Session, model) -> int:
    count = db.query(model).count()
    return count
