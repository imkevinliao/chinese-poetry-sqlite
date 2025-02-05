# 中华诗词文化
千年文化传承

# 部署&运行
环境准备：Python Verion = 3.12

安装必要库：pip install -r requirement.txt

运行:python fastapi_main.py

# 补充
1. 端口冲突，修改端口：fastapi_main.py 中 uvicorn.run("fastapi_main:app", host='0.0.0.0', port=8000, reload=False), 调整 port 即可



