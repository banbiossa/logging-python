# test logging


## 仮説
python の logging ではログを吐く側は適当に logger.info でよくて、受け取る側が basicConfig でよしなに設定する

## 検証方法
- logging-server は適当なログをはく.
- logging-client は logging-server を import して適当な cli を実行する
- logging-server のログがどうやったら見えるか検証する


## メモ
logging-server を２パターン用意したほうがいいかも？


