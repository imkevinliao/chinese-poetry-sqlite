import os
import time

import opencc
from sqlalchemy.orm import Session

from . import crud
from .data import get_datas
from .database import get_db
from .schemas import *
from . import models


async def fill_sqlite(root_path):
    if root_path is None:
        return None
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    
    db: Session = next(get_db())  # 获取数据库会话
    wdsc_hj_path = os.path.join(root_path, "五代诗词", "huajianji")
    wdsc_hj_regex = r"huajianji-(?!0-)[a-zA-Z0-9]+-juan\.json"
    datas = get_datas(wdsc_hj_path, wdsc_hj_regex)
    for data in datas:
        create_data = CreateWuDaiShiCiHuaJian(**data)  # 数据应当通过 Pydantic 模型进行解析
        crud.create_WuDaiShiCiHuaJian(db, data=create_data)  # 正确调用 CRUD 函数
    count = crud.count_records(db, models.WuDaiShiCiHuaJian)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{wdsc_hj_path}")
    
    yq_path = os.path.join(root_path, "元曲")
    yq_regex = r"yuanqu\.json"
    datas = get_datas(yq_path, yq_regex)
    for data in datas:
        create_data = CreateYuanQu(**data)
        crud.create_YuanQu(db, data=create_data)
    count = crud.count_records(db, models.YuanQu)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{yq_path}")
    
    sc_path = os.path.join(root_path, "宋词")
    sc_regex = r"ci.song.\d+\.json"
    datas = get_datas(sc_path, sc_regex)
    for data in datas:
        create_data = CreateSongCi(**data)
        crud.create_SongCi(db, data=create_data)
    count = crud.count_records(db, models.SongCi)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{sc_path}")
    
    cc_path = os.path.join(root_path, "楚辞")
    cc_regex = r"chuci\.json"
    datas = get_datas(cc_path, cc_regex)
    for data in datas:
        create_data = CreateChuCi(**data)
        crud.create_ChuCi(db, data=create_data)
    count = crud.count_records(db, models.ChuCi)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{cc_path}")
    
    ly_path = os.path.join(root_path, "论语")
    ly_regex = r"lunyu\.json"
    datas = get_datas(ly_path, ly_regex)
    for data in datas:
        create_data = CreateLunYu(**data)
        crud.create_LunYu(db, data=create_data)
    count = crud.count_records(db, models.LunYu)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{ly_path}")
    
    sj_path = os.path.join(root_path, "诗经")
    sj_regex = r"shijing\.json"
    datas = get_datas(sj_path, sj_regex)
    for data in datas:
        create_data = CreateShiJing(**data)
        crud.create_ShiJing(db, data=create_data)
    count = crud.count_records(db, models.ShiJing)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{sj_path}")
    
    # 全唐诗比较特殊，原始数据是繁体，我替换成简体，同时保留原始数据 （数据量太大）
    qts_path = os.path.join(root_path, "全唐诗")
    qts_regex = r"poet.(tang|song).\d+\.json"
    datas = get_datas(qts_path, qts_regex)
    converter = opencc.OpenCC('t2s')
    # 单条插入太慢了
    # for index, data in enumerate(datas):
    #     data["author_origin"] = data.get("author", "")
    #     data["paragraphs_origin"] = data.get("paragraphs", "")
    #     data["note_origin"] = data.get("note", "")
    #     data["title_origin"] = data.get("title", "")
    #     data["author"] = converter.convert(data.get("author", ""))
    #     data["paragraphs"] = converter.convert(data.get("paragraphs", ""))
    #     data["note"] = converter.convert(data.get("note", ""))
    #     data["title"] = converter.convert(data.get("title", ""))
    #     create_data = CreateQuanTangShi(**data)
    #     crud.create_QuanTangShi(db, data=create_data, ignore_query=False)
    
    temp_list = []
    each_count = 1000
    total_count = len(datas)
    for index, data in enumerate(datas):
        # 为每条数据添加原始字段
        data["author_origin"] = data.get("author", "")
        data["paragraphs_origin"] = data.get("paragraphs", "")
        data["note_origin"] = data.get("note", "")
        data["title_origin"] = data.get("title", "")
        
        # 使用转换器转换字段
        data["author"] = converter.convert(data.get("author", ""))
        data["paragraphs"] = converter.convert(data.get("paragraphs", ""))
        data["note"] = converter.convert(data.get("note", ""))
        data["title"] = converter.convert(data.get("title", ""))
        
        # 创建模型实例
        create_data = CreateQuanTangShi(**data)
        temp_list.append(create_data)
        
        # 每 1000 条数据插入一次，且确保最后一批数据也能插入
        if (index + 1) % each_count == 0 or (index == total_count - 1):
            # 批量插入数据
            crud.create_QuanTangShi_batch(db, data_list=temp_list, ignore_query=False)
            # 清空临时列表
            temp_list = []
    
    count = crud.count_records(db, models.QuanTangShi)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 共计 {count} 条数据已经创建完毕：{qts_path}")
