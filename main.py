#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from sys import argv, exit
from rich.console import Console
from time import sleep
import urllib.request
from json import dumps





console = Console()
proxy_list = []
final_list=[]
ua = generate_user_agent(os=('mac', 'linux', 'win'))



def banner():
    banr = r"""
______                         _   _ _       _                          
| ___ \                       | \ | (_)     (_)                         
| |_/ / __ _ __ _____  ___   _|  \| |_ _ __  _  __ _ ______ _ __   __ _ 
|  __/ '__| '__/ _ \ \/ / | | | . ` | | '_ \| |/ _` |______| '_ \ / _` |
| |  | |  | | | (_) >  <| |_| | |\  | | | | | | (_| |      | | | | (_| |
\_|  |_|  |_|  \___/_/\_\\__, \_| \_/_|_| |_| |\__,_|      |_| |_|\__, |
                          __/ |            _/ |                    __/ |
                         |___/            |__/                    |___/ 
"""
    console.print(f"[cyan bold]{banr}[/cyan bold]")
    console.print("\t\t  [cyan bold]Fetch Latest [magenta bold]Https/Socks4/Socks5[/magenta bold] Proxies[/cyan bold]")
    console.print("[yellow bold]_[/yellow bold]" * 80 + "\n")


def check_internet_conn():
    try:
        console.print("\n[" + "[blue bold]Info[/blue bold]" + "]" + "[red bold] Checking for Internet Connection...[/red bold]")
        host = "https://www.google.com"
        urllib.request.urlopen(host)
        console.print("[" + "[blue bold]Info[/blue bold]" + "]" + " Connection:[green bold] Connected...[/green bold]")
    except:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + " Connection:[bold] No Internet Connection...[/bold]")
        exit(1)


def help():
    console.print("\n\t\t\t[green_yellow bold]<<< Help for Proxy Ninja - NG >>>[/green_yellow bold]")
    console.print("""[red bold]Options:[/red bold]
        [yellow bold]Primary:-[/yellow bold] 
            -t      Proxy Type              (Proxy Type https/socks4/socks5)
            -o      Filename                (Output Filename)
            -f      Format                  (Output File Format [txt,json])
    """)
    exit(0)


def listTodict(final_list):
    global res_dct
    res_dct = []
    for proxy_port in final_list:
        _lst = proxy_port.split(':')
        dct = {
            "IP Address": _lst[0],
            "Port": _lst[1]
        }
        res_dct.append(dct)
    return res_dct


def iO_func(final_list, proxy_type, output_filename, output_format):
    try:
        _filename = f"{output_filename}_{proxy_type}.{output_format}"
        if output_format == "json":
            listTodict(final_list)
            with open(_filename, "w+") as handle:
                handle.write(dumps(res_dct))
        else:
            with open(_filename, "w+") as handle:
                for proxy in final_list:
                    handle.write(str(proxy) + "\n")
    except Exception as err:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
        exit(1)



def get_url(ua, URL):
    temp_list = []
    s = requests.Session()
    if len(URL) != 0:
        for url in URL:
            try:
                s.headers.update({
                            "user-agent": f"{ua}",
                            "Accept-Encoding": "*",
                            "Connection": "keep-alive"
                        })
                r = s.get(url)
                soup = BeautifulSoup(r.content, 'html5lib')
                for row in soup.table.find_all('tr')[1:]:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    temp_list.append([ele for ele in cols if ele])
                for i in range(len(temp_list)):
                    proxy = f"{temp_list[i][0]}:{temp_list[i][1]}"
                    if proxy not in proxy_list:
                        proxy_list.append(proxy)
                return proxy_list
            except Exception as err:
                console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
                exit(1)



def get_api(ua, api):
    temp_list = []
    try:
        s = requests.Session()
        s.headers.update({
                    "user-agent": f"{ua}",
                    "Accept-Encoding": "*",
                    "Connection": "keep-alive"
                        })
        r = s.get(api)
        temp_list = r.content.decode('utf-8').splitlines()
        for proxy in temp_list:
            if proxy not in proxy_list:
                proxy_list.append(proxy)
        return proxy_list
    except Exception as err:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
        exit(1)



def get_uniQ(proxy_list):
    if len(proxy_list) > 0:
        for proxy in proxy_list:
            if proxy not in final_list:
                final_list.append(proxy)
    return final_list


def get_http_https(ua):
    URL = [
    "https://sslproxies.org", 
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234#list", 
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234&start=64#list",
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234&start=128#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=https"
    
    get_url(ua, URL)
    get_api(ua, api)



def get_socks4(ua):
    URL = [
    "https://www.socks-proxy.net", 
    "https://hidemy.name/en/proxy-list/?type=4&anon=1234#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=socks4"
    
    get_url(ua, URL)
    get_api(ua, api)



def get_socks5(ua):
    URL = ["https://hidemy.name/en/proxy-list/?type=5&anon=1234#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=socks5"
    
    get_url(ua, URL)
    get_api(ua, api)



def main():
    args = argv
    if len(args) == 2:
            if argv[1] == "-h" or argv[1] == "--help":
                help()
    elif len(args) == 7:
        if (str(argv[2])).lower() == "https" or (str(argv[2])).lower() == "socks4" or (str(argv[2])).lower() == "socks5":
            proxy_type = str(argv[2])
            output_filename = str(argv[4])
            if (str(argv[6])).lower() == "txt" or (str(argv[6])).lower() == "json":
                output_format = str(argv[6])
                console.print(f"""
                Arguments:-
                    [green bold]Proxy Type:\t\t\t[/green bold][cyan]{proxy_type}[/cyan]
                    [green bold]Output Filename:\t\t[/green bold][cyan]{output_filename}[/cyan]
                    [green bold]Output Format:\t\t[/green bold][cyan]{output_format}[/cyan]
                """)
                console.print("=+=" * 30)
                check_internet_conn()
                sleep(1)
                console.print("[" + "[blue bold]Info[/blue bold]" + "]" + " Fetching User-Agent List..")
                sleep(2)
                if proxy_type == "https":
                    get_http_https(ua)
                    get_uniQ(proxy_list)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" {len(final_list)} Proxie(s) are Successfully Scraped..")
                    sleep(1)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" Saving Proxies in [green bold]{output_filename}_{proxy_type}.{output_format}[/green bold] file..")
                    iO_func(final_list, proxy_type, output_filename, output_format)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + " Proxies Saved Sucessfully..\n")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" [cyan bold]File Saved: [/cyan bold]{output_filename}_{proxy_type}.{output_format}..")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
                elif proxy_type == "socks4":
                    get_socks4(ua)
                    get_uniQ(proxy_list)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" {len(final_list)} Proxie(s) are Successfully Scraped..")
                    sleep(1)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" Saving Proxies in [green bold]{output_filename}_{proxy_type}.{output_format}[/green bold] file..")
                    iO_func(final_list, proxy_type, output_filename, output_format)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + " Proxies Saved Sucessfully..\n")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" [cyan bold]File Saved: [/cyan bold]{output_filename}_{proxy_type}.{output_format}..")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
                else:
                    get_socks5(ua)
                    get_uniQ(proxy_list)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" {len(final_list)} Proxie(s) are Successfully Scraped..")
                    sleep(1)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" Saving Proxies in [green bold]{output_filename}_{proxy_type}.{output_format}[/green bold] file..")
                    iO_func(final_list, proxy_type, output_filename, output_format)
                    sleep(2)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + " Proxies Saved Sucessfully..\n")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
                    console.print("[" + "[blue bold]Info[/blue bold]" + "]" + f" [cyan bold]File Saved: [/cyan bold]{output_filename}_{proxy_type}.{output_format}..")
                    console.print("[magenta bold]=+=[/magenta bold]" * 30)
            else:
                console.print("[" + "[red bold]Error[/red bold]" + "]" + "[bold blink] Wrong Argument Value, [yellow]Format[/yellow] should only be (txt) or (json)...![/bold blink]")
                help()
        else:
            console.print("[" + "[red bold]Error[/red bold]" + "]" + "[bold blink]Wrong Argument Value, [yellow]Proxy Type[/yellow] should only be https/socks4/socks5...![/bold blink]")
            help()
    else:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + "[bold blink] Argument Missing...![/bold blink]")
        help()



if __name__ == '__main__':
    banner()
    main()