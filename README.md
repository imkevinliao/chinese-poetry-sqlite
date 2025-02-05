# 中华诗词文化
千年文化传承 ×

不过是个喜欢读读诗词的平凡人 √
# 部署&运行
环境准备：Python Verion = 3.12

安装必要库：pip install -r requirement.txt

运行:python fastapi_main.py

补充（ubuntu）部署 Python3.12 及 pip3.12 参考：https://github.com/imkevinliao/UbuntuDocs/blob/master/markdown/python.md
# 高级
1. 端口冲突，修改端口：fastapi_main.py 中 uvicorn.run("fastapi_main:app", host='0.0.0.0', port=8000, reload=False), 调整 port 即可

2. 自行生成数据库：删除旧的数据 culture_sqlite.db， culture/core.py 指定仓库路径即可 root_path = None

3. 数据库配置：culture/database.py

4. 数据源：https://github.com/chinese-poetry/chinese-poetry  已在子模块中 third-repository/chinese-poetry
# 寄语

很早就做过了，一开始是裸写 sql 语句，到后来用 sqlalchmy orm，再到现在使用 fastapi 构建。

人生的路，不知道哪一天就串起来了。
