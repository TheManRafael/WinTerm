@echo off
pip install pyinstaller
pip install -r requirements.txt
pyinstaller --onefile main.py --add-data "C:\Users\%username%\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet;./pyfiglet"
pause