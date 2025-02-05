import json
import os
import re
from typing import Optional, Dict, Any


def convert_to_str(data: Dict[str, Any]) -> Dict[str, str]:
    """
    将字典中的值转换为字符串类型，处理列表和空值的情况。
    """
    result = {}
    
    for key, value in data.items():
        if isinstance(value, list):
            # 如果是列表，连接成字符串
            result[key] = " ".join(map(str, value)) if value else "None"
        elif value is None:
            # 如果值是 None，设置为 "None" 或其他默认值
            result[key] = "None"
        else:
            # 否则直接转换为字符串
            result[key] = str(value)
    
    return result


def parse_json(filepath: str) -> Optional[list[dict]]:
    with open(filepath, 'r', encoding="utf-8") as f:
        json_data = json.load(f)
    datas = []
    for data in json_data:
        dict_value2str = convert_to_str(data)  # 直接转成str，后面pydantic可以直接解包使用
        datas.append(dict_value2str)
    return datas


def get_path_by_regex(path: str, regex: str) -> Optional[list[str]]:
    files = os.listdir(path)
    result = []
    for file in files:
        if re.match(regex, file):
            temp = os.path.join(path, file)
            result.append(temp)
    return result


def get_path_by_keyword(path: str, keyword: str) -> Optional[list[str]]:
    files = os.listdir(path)
    result = []
    for file in files:
        if keyword in file:
            temp = os.path.join(path, file)
            result.append(temp)
    return result


def get_path_by_exclude(path: str, keyword: str) -> Optional[list[str]]:
    files = os.listdir(path)
    result = []
    for file in files:
        if keyword in file:
            ...
        else:
            temp = os.path.join(path, file)
            result.append(temp)
    return result


def get_datas(path: str, regex: str) -> list:
    datas = []
    files = get_path_by_regex(path, regex)
    for file in files:
        data = parse_json(file)
        datas.extend(data)
    return datas
