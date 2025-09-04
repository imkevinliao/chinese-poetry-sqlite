# 中华诗词文化
为了千年文化传承（宏大目标） ×

闲来读读诗词的俗人（微小叙事） √

万物皆可 docker，一条命令直接部署：

```
docker run -d --restart=always -p 8000:8000 --name culture kevinstarry/culture 
```
# 开发参考
环境准备：Python Verion = 3.12

新建一个空文件夹（进入空文件夹）

克隆仓库：`git clone https://github.com/imkevinliao/chinese-poetry-sqlite.git .`

安装必要库：`pip install -r requirements.txt`

直接下载sqlite数据（放置在仓库下）：`curl -L https://github.com/imkevinliao/chinese-poetry-sqlite/releases/download/v1.0/culture_sqlite.db -o ./culture_sqlite.db`

运行:python fastapi_main.py

补充（ubuntu）部署 Python3.12 及 pip3.12 参考：https://github.com/imkevinliao/UbuntuDocs/blob/master/markdown/python.md
# 高级
1. 端口冲突，修改端口：fastapi_main.py 中 修改 port 为其他端口
2. 准备数据：获取子仓库数据：git submodule init && git submodule update
3. 配置数据源：culture/core.py  root_path = None 修改为注释值即可，生成后记得置None
4. 数据库配置：culture/database.py
5. 数据源：https://github.com/chinese-poetry/chinese-poetry  已在子模块中 third-repository/chinese-poetry
6. 本地测试:uvicorn fastapi_main:app --host 127.0.0.1 --port 8000 --reload

# 尾声
喜欢诗词的庸人
