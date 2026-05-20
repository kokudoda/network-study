# network-study

Docker・Linux・ネットワーク技術の学習用リポジトリです。

## Directory Structure

```text
network-study/
├── docker/
│   ├── client_server/
│   └── docker-ping-monitor/
│
└── packet_tracer/
    ├── ARP/
    ├── NAPT/
    ├── VLAN/
    └── VPN/
```
# docker

## client_server

Docker コンテナ間通信の確認環境。

- nginx サーバー
- Ubuntu クライアント
- tcpdump によるパケットキャプチャ
- Wireshark で TCP 3-way handshake を確認

---

## docker-ping-monitor

Python を用いた ping 監視環境。

- クライアントから定期的に ping を送信
- OK / NG 表示
- Docker Compose による自動実行

---

# packet_tracer

Cisco Packet Tracer を用いたネットワーク学習。

- ARP
- NAPT
- VLAN
- VPN
