FROM python:3.12-slim

WORKDIR /app

RUN apt update && apt install -y git tzdata curl cmake build-essential libffi-dev libz-dev && \
    timedatectl set-timezone Asia/Shanghai

RUN git clone https://github.com/imkevinliao/chinese-poetry-sqlite.git . && \
    pip install --upgrade pip && pip install -r requirements.txt

RUN curl -L https://github.com/imkevinliao/chinese-poetry-sqlite/releases/download/v1.0/culture_sqlite.db -o ./culture_sqlite.db

EXPOSE 8000

CMD ["python", "fastapi_main.py"]
