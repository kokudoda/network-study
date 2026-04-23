## 構成
- web1: nginxサーバー
- web2: nginxサーバー
- client: curlでリクエストを送るコンテナ

## 起動方法
docker compose up -d

##　通信の確認方法
clientコンテナに入ります
docker compose exec client sh

web1にリクエストを送ります
curl http://web1

web2にリクエストを送ります
curl http://web2

## パケットキャプチャの方法

### 1. web1コンテナ(またはweb2コンテナ)に入ります
docker compose exec web1 bash (web2なら、docker compose exec web2 bash)

### 2. tcpdumpをインストール
apt-get update && apt-get install -y tcpdump

### 3. キャプチャ開始
tcpdump -i eth0 -nn -w /tmp/capture.pcapng

### 4. 別ターミナルでリクエストを送る
docker compose exec client sh
curl http://web1

### 5. Ctrl+Cでキャプチャ停止後、ファイルを取り出す
docker compose cp web1:/tmp/capture.pcapng ./capture.pcapng

## 観察したこと
- TCPの3ウェイハンドシェイク
- HTTPのGETリクエストとレスポンス
- FIN後のユニキャストARP

## 学んだこと
- DockerのブリッジネットワークでのTCP/HTTP通信
- tcpdumpでパケットキャプチャしWiresharkで観察


'''mermaid
graph TD
    client -->|HTTP port8080| web1
    client -->|HTTP port8081| web2
    web1 -->|index1.html| client
    web2 -->|index2.html| client

    subgraph Docker Neteork
        web1[web1 : nginx]
        web2[web2 : nginx]
        clinet[clinet : curl]
    end
'''

