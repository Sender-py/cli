import click
import requests
from colorama import Fore
import json
banner = r"""
.▄▄ · ▄▄▄ . ▐ ▄ ·▄▄▄▄  ▄▄▄ .▄▄▄      ▄▄▄· ▄· ▄▌
▐█ ▀. ▀▄.▀·•█▌▐███▪ ██ ▀▄.▀·▀▄ █·   ▐█ ▄█▐█▪██▌
▄▀▀▀█▄▐▀▀▪▄▐█▐▐▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄     ██▀·▐█▌▐█▪
▐█▄▪▐█▐█▄▄▌██▐█▌██. ██ ▐█▄▄▌▐█•█▌   ▐█▪·• ▐█▀·.
 ▀▀▀▀  ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ .▀  ▀ ▀ .▀     ▀ • 

"""
@click.group()
def cli():
 print(Fore.WHITE + banner)
 print(Fore.RED + "Welcome to Sender.py!")
 print(Fore.GREEN + r"""
Usage:
python sender.py get --t example.com
With Bearer Token:
python sender.py getwithtoken --t example.com --auth 123456789
 """)
 print(Fore.BLUE + "Made", Fore.WHITE + "In", Fore.RED + "France")
 print(Fore.WHITE + "https://github.com/Sender-py")

## GET 
@cli.command()
@click.option('--t', help='Target')
def get(t):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.get(t)
 print(Fore.GREEN + "HTTP Code:", r.status_code)
 print("Response:", r.text)
## POST
@cli.command()
@click.option('--t', help='Target')
@click.option('--data', help='JSON')
def post(t, data):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.post(t, json=json.loads(data))
 print(Fore.GREEN + "HTTP Code:", r.status_code)
## PUT
@cli.command()
@click.option('--t', help='Target')
@click.option('--data', help='JSON')
def put(t, data):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.put(t, json=json.loads(data))
 print(Fore.GREEN + "HTTP Code:", r.status_code)
## DELETE
@cli.command()
@click.option('--t', help='Target')
def delete(t):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.delete(t)
 print(Fore.GREEN + "HTTP Code:", r.status_code)
## GET 
@cli.command()
@click.option('--t', help='Target')
@click.option('--auth', help='Bearer Token')
def getwithtoken(t, auth):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.get(t, headers={
    "Authorization": auth
 })
 print(Fore.GREEN + "HTTP Code:", r.status_code)
 print("Response:", r.text)
## POST
@cli.command()
@click.option('--t', help='Target')
@click.option('--auth', help='Bearer Token')
@click.option('--data', help='JSON')
def posttwithtoken(t, auth, data):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.post(t, headers={
    "Authorization": auth
 }, json=json.loads(data))
 print(Fore.GREEN + "HTTP Code:", r.status_code)
 print("Response:", r.text)
## PUT
@cli.command()
@click.option('--t', help='Target')
@click.option('--auth', help='Bearer Token')
@click.option('--data', help='JSON')
def putwithtoken(t, auth, data):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.put(t, headers={
    "Authorization": auth
 }, json=json.loads(data))
 print(Fore.GREEN + "HTTP Code:", r.status_code)
 print("Response:", r.text)
## DELETE
@cli.command()
@click.option('--t', help='Target')
@click.option('--auth', help='Bearer Token')
def deletewithtoken(t, auth):
 if not t.startswith("http"):
    t = "http://" + t
 r = requests.delete(t, headers={
    "Authorization": auth
 })
 print(Fore.GREEN + "HTTP Code:", r.status_code)
 print("Response:", r.text)




if __name__ == '__main__':
    cli()