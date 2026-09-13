from PIL import Image
import pytesseract
from decimal import Decimal
print('##  Program Python Menghitung Luas Persegi  ##')
print('==============================================')
y = input()
try:
     print(eval(y))
except (RuntimeError, TypeError, NameError):
     pass