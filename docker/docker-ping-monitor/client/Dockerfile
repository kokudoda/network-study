FROM ubuntu:latest

#pingと.pyファイルを使うのでインストール
RUN apt-get update && apt-get install -y iputils-ping python3

WORKDIR /app

COPY ping_check.py .

CMD ["python3","ping_check.py"]