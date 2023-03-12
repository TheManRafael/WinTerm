# WinTerm

WinTerm is python terminal application that recreats Linux terminal in Windows. 

## Installation
Download [exe file](https://raw.githubusercontent.com/TheManRafael/WinTerm/main/main.exe) and run it \
Or run as normal python file. If runing pure python file please note that command "sudo" will probably not work!
To install WinTerm just clone the Repository or download it

```bash
git clone https://github.com/TheManRafael/WinTerm.git
```
Install all required packages with pip in the requirements.txt.
```bash
pip install -r requirements.txt
```
Now run the python program and you are ready to go.
```bash
python main.py
```
Please note that you can only run this program if you have python. We are planning a exe file but for now you will need to make from source. Also do not run this script with Python Idle since terminal will not show up properly.

## Commands
"netsh" wlan and internet tools \
"exit" exit terminal \
"say" prints given text in the terminal \
"echo" prints give test in terminal and can save them to file \
"help" prints help \
"dir" show current dir add to cange dir \
"cd" changes the current dir \
"ls" show files and dir in a dir \
"shutdown" shuts down the device \
"restart" restarts the device \
"msg" shows a messagebox \
"vol" shows details about Windows Installation Drive \
"apt" installation package \
"chos" compars os from windows \
"clear" clears the current screen \
"title" changes the title of the screen \
"start" start program or webpage \
"cmd" start cmd and execute commands \
"notepad" starts notepad/file \
"pprint" makes a decorated print \
"fprint" print files content \
"sudo" runs the terminal as administrator \
"whoami" tells you who is running the program \
"wget" Download files in current dir from the internet \
"rm" delete file or directories

## Build for Source

Download the repository or clone it.

```bash
git clone https://github.com/TheManRafael/WinTerm.git
```
Before you build make sure you have pyinstaller installed and other needed packages!

```bash
pip install pyinstaller
pip install -r requirements.txt
```
Make sure you are in the folder with all the files. Then run this build command with pyinstaller.
```bash
pyinstaller --onefile main.py --add-data "C:\Users\%username%\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet;./pyfiglet"
```
Now navigate into the exe build folder.
```bash
cd dist
```
Now you can run the exe file. If you have any issues go an open a issue

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
