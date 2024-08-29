# feed_client.py

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Specification](#specification)
4. [License](#license)
5. [Contact](#contact)

## Overview  
このスクリプトは、[SYNESIS](https://www.synesis.tech/{:target=”_blank”}) FeedServiceで使用するサンプルスクリプトです。  
Feed Serviceとは、ソケットを介してSYNESISがキャプチャしたパケットを読み出す仕組みです。

## Architecture  

Feed Serviceの仕組みを下図に示します。  
![image](https://github.com/user-attachments/assets/a2b286ca-09b2-4730-ba21-1046c8a6371d)

1. SYNESIS/キャプチャ：ネットワークカードからパケットを受信します
2. SYNESIS/キャプチャ：受信パケットをパケットデータ領域に保存します
3. クライアント/クライアントプログラム：TCP/IPでSYNESIS/Feed Serviceに対してパケットの要求をします
4. SYNESIS/Feed Service：パケットデータ領域からパケットを読み出します
5. SYNESIS/Feed Service：TCP/IPで要求元に対してパケットを送信します

## Specification 

| オプション           | 説明                                                                                       | 値の設定範囲                                      | 省略時のデフォルト値            |
|----------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------|---------------------------------|
| `-h`, `--help`       | ヘルプを表示します。                                                                         | -                                                 | -                               |
| `-f`, `--format`     | ファイルフォーマットを指定します。                                                            | `pcap`: pcap(ナノ秒)形式<br>`pcapng`: pcapng形式<br>`scap`: scap形式 | `pcap`                          |
| `-c`, `--channels`   | チャネルを指定します。                                                                       | `A～H`, または`all`<br>複数のチャネルを使用する場合はスペースで区切って指定してください | `A`                             |
| `-a`, `--address`    | SYNESISのIPアドレスを指定します。                                                            | IPv4アドレス                                      | `127.0.0.1`                     |
| `-p`, `--port`       | Feed ServiceのTCPポートを指定します。                                                        | 1～65535の整数                                     | `9060`                          |
| `-s`, `--start`      | 読み出しの開始時刻を指定します。                                                             | `0` または `YYYY-mm-dd_HH-MM-SS`<br>`0`を指定した場合は、直近のキャプチャレコードの先頭から読み出します。 | `0`                             |
| `-e`, `--end`        | 読み出しの終了時刻を指定します。                                                             | `0` または `YYYY-mm-dd_HH-MM-SS`<br>`0`を指定した場合は、直近のキャプチャレコードの後尾まで読み出します。もしキャプチャが継続している場合は、受信パケットをリアルタイムで読み出します。 | `0`                             |
| `-z`, `--size`       | クライアントが受信可能なメッセージの最大サイズをKB単位で指定します。                            | `1` 以上の整数                                     | `1`                             |
| `-o`, `--output`     | 受信パケットを出力するファイル名を指定します。                                               | ファイル名                                        | 標準出力へパケットを出力します |

## License  
© TOYO Corporation  
Licensed under the [MIT License](https://github.com/synesis-toyo/FeedService?tab=MIT-1-ov-file).

## Contact
[synesis-globalsales@toyo.co.jp](<mailto:synesis-globalsales@toyo.co.jp>)



