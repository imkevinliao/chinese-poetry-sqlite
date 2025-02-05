from sqlalchemy import Column, Integer, String, DateTime, func, Text

from .database import Base


class WuDaiShiCiHuaJian(Base):
    __tablename__ = 'WuDaiShiCiHuaJian'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    paragraphs = Column(Text)
    author = Column(String(255))
    rhythmic = Column(String(255))
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


# class WuDaiShiCiNanTang(Base):
#     __tablename__ = "WuDaiShiCiNanTang"


class YuanQu(Base):
    __tablename__ = "YuanQu"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dynasty = Column(String(255))
    author = Column(String(255))
    paragraphs = Column(Text)
    title = Column(String(255))
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


class QuanTangShi(Base):
    # 全唐诗是繁体存储，我们通常使用简体（转换后），但保留一份原始数据
    __tablename__ = "QuanTangShi"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author = Column(String(255))
    paragraphs = Column(Text)
    note = Column(Text)
    title = Column(String(255))
    
    # 原始数据
    author_origin = Column(String(255))
    paragraphs_origin = Column(Text)
    note_origin = Column(Text)
    title_origin = Column(String(255))
    
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


# class SiShuWuJin(Base):
#     __tablename__ = "SiShuWuJin"


class SongCi(Base):
    __tablename__ = "SongCi"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author = Column(String(255))
    paragraphs = Column(Text)
    rhythmic = Column(String(255))
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


# class YouMengYin(Base):
#     __tablename__ = "YouMengYin"


# class YuDingQuanTangShi(Base):
#     __tablename__ = "YuDingQuanTangShi"


# class CaoCaoShiJi(Base):
#     __tablename__ = "CaoCaoShiJi"


class ChuCi(Base):
    __tablename__ = "ChuCi"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    section = Column(String(255))
    author = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


# class ShuiMoTangShi(Base):
#     ...
#
#
# class NaLanXinDe(Base):
#     ...
#
#
# class MengXue(Base):
#     ...


class LunYu(Base):
    __tablename__ = "LunYu"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chapter = Column(String(255))
    paragraphs = Column(Text)
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')


class ShiJing(Base):
    __tablename__ = "Shijing"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    chapter = Column(String(255))
    section = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')
