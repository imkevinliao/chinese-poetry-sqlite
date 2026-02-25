# docker
```
docker run -d --restart=always -p 8000:8000 --name culture kevinstarry/culture 
```
# 开发
环境准备：Python Verion = 3.12

新建一个空文件夹，克隆仓库：`git clone https://github.com/imkevinliao/chinese-poetry-sqlite.git .`

安装必要库：`pip install -r requirements.txt`

下载sqlite数据：`curl -L https://github.com/imkevinliao/chinese-poetry-sqlite/releases/download/v1.0/culture_sqlite.db -o ./culture_sqlite.db`

运行:python fastapi_main.py
# 补充
获取子仓库数据：git submodule init && git submodule update

本地测试:uvicorn fastapi_main:app --host 127.0.0.1 --port 8000 --reload
