# ISBN13 Barcode's create program for Raspberry Pi OS
# $ sudo apt install python3-pip
# $ pip3 install python-barcode
# $ python3 -m pip install --upgrade pip
# $ python3 -m pip install --upgrade Pillow
# $ python3 barcode_create.py [ISBN13] [Vol numbar(example:vol68)]
# Two files is created, SVG and Png. 
import barcode
from barcode.writer import ImageWriter
from barcode import generate
import sys

bar_code = sys.argv[1]
file_name = sys.argv[2]
code_format = 'isbn13'

bar_code_class = barcode.get_barcode_class(code_format) 
bar_code_make = bar_code_class(bar_code, writer=ImageWriter()) 
bar_code_png = bar_code_make.save(file_name) 
bar_code_svg = generate(code_format, bar_code, output=file_name)
