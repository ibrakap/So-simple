#!/usr/bin/env python3
import sys
import urllib.request

def parse_test(file_name):
    clear = ""
    with open("{0}".format(file_name),"r") as file:
        clear += file.read()
    clear = clear.splitlines()
    return clear

def info():
    print("""This program was desinged by ibrakap

Usage:

For windows
|-----------------------|
|dirb.py <url> <keylist>|
|-----------------------|

Linux or Mac Os
|-----------------------|
|./dirb <url> <keylist> |
|-----------------------|

Or

|-------------------------------|
|python3 dirb.py <url> <keylist>|
|-------------------------------|
""")

def main():
    succes = 0
    unsucces = 0
    try:
        now = True
        url = str(sys.argv[1])
        if url.startswith("https://") or url.startswith("http://"):
            pass
        else:
            while now:
                choose = input("which http[1] or https[2]: ")
                if choose == "1":
                    url = "http://" + url
                    now = False
                elif choose == "2":
                    url = "https://" + url
                    now = False
                else:
                    print("Select one!")
        keywords = parse_test(sys.argv[2])
        for i in keywords:
            try:
                requests = urllib.request.Request(url+i,None,headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
                return_code = urllib.request.urlopen(requests).getcode()
                print(url+i,"=>",return_code)
                succes += 1
            except urllib.error.HTTPError as http:
                print(url+i,"=>",404)
                unsucces += 1
            except:
                print(url+i,"=>",404)
                unsucces += 1
        print("Result succes {0}  unsucces {1}".format(succes,unsucces))
    except IndexError:
        info()
if __name__ == "__main__":
    main()