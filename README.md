# ISBN13のバーコードを作成するPythonプログラム
ISBN13の番号からSVG形式とPNG形式のバーコードファイルを作成します。稼働環境は、Raspberry Pi OSとしていますが、Linux系OSやWindowsでも動作します。
「python-barcode」モジュールを利用するので、次のようにインストールします。また、Pillowモジュールのアップデートも必要です。

$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade Pillow  
$ pip3 install python-barcode  

「barcode_create.py」は、次のように実行します。

$ python3 barcode_create.py ISBN13の番号 ファイル名

ファイル名.svgとファイル名.pngというファイルが生成されます。

