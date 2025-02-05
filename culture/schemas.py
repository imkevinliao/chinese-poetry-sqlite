from datetime import datetime

from pydantic import BaseModel


class CreateWuDaiShiCiHuaJian(BaseModel):
    title: str
    paragraphs: str
    author: str
    rhythmic: str
    notes: str


class ReadWuDaiShiCiHuaJian(CreateWuDaiShiCiHuaJian):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateYuanQu(BaseModel):
    dynasty: str
    author: str
    paragraphs: str
    title: str


class ReadYuanQu(CreateYuanQu):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateQuanTangShi(BaseModel):
    # 简体数据
    author: str
    paragraphs: str
    note: str
    title: str
    
    # 繁体数据（原始）
    author_origin: str
    paragraphs_origin: str
    note_origin: str
    title_origin: str


class ReadQuanTangShi(CreateQuanTangShi):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateSongCi(BaseModel):
    author: str
    paragraphs: str
    rhythmic: str


class ReadSongCi(CreateSongCi):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateChuCi(BaseModel):
    title: str
    section: str
    author: str
    content: str


class ReadChuCi(CreateChuCi):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateLunYu(BaseModel):
    chapter: str
    paragraphs: str


class ReadLunYu(CreateLunYu):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True


class CreateShiJing(BaseModel):
    title: str
    chapter: str
    section: str
    content: str


class ReadShiJing(CreateShiJing):
    id: int
    updated_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True
