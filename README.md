# ISBN13のバーコードを作成するPythonプログラム
ISBN13の番号からSVG形式とPNG形式のバーコードファイルを作成します。稼働環境は、Raspberry Pi OSとしていますが、Linux系OSやWindowsでも動作します。
「python-barcode」モジュールを利用するので、次のようにインストールします。

$ pip3 install python-barcode

「barcode_create.py」は、次のように実行します

$ python3 barcode_create.py <span style="color: blue; ">ISBN13の番号</span> <span style="color: blue; ">ファイル名</span>

