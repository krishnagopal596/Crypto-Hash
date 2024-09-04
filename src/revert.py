import os
from shutil import copyfile
from pathlib import Path

img = Path('images/tajoriginal.jpeg')

if img.exists():
    copyfile('original/tajoriginal.jpeg', 'images/tajoriginal.jpeg')
else:
    os.rename('images/notsoimportant.jpeg', 'images/tajoriginal.jpeg')

