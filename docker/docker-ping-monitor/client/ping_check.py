import subprocess
import time

#宛先のホスト名
hosts = ["web1","web2"]

while True:
    print("========== ping check ==========")

    for host in hosts:
        
        #pingコマンド(各ホストに1回pingを送る)
        args = ["ping",host,"-c","1"]

        #subprocess.run()はシステムのシェルコマンドや他のプログラムを実行できる関数
        #capture_output=True　はコマンドの標準出力と標準エラー出力をキャプチャできる
        #text=True 　は出力を文字列として取得。デフォルトではバイト列となっている
        result = subprocess.run(args,capture_output=True,text=True)

        #returncodeが0で正常終了
        if result.returncode == 0:
            print(f"{host} : OK")
            #print(result.stdout)
        else:
            print(f"{host} : NG")
    
    time.sleep(10) #10秒ごと