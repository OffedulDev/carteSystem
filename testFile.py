import barcode
import shutil
from checkdigit import verhoeff

t = verhoeff.calculate(str(42424242420))

print(t)
