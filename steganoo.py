#Dhia Hauzan Muafa 2301926245
from getopt import getopt
import sys
import subprocess

DATA = ""
IMAGE = ""
STEGANO = False
GET = False


def steg():
    comm = input("Input Command: ")

    arg = f"exiftool -Comment='{comm}' {IMAGE}"

    process = subprocess.Popen(
        args=arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if stderr != b'':
        print(stderr)
    else:
        pass


def get():
    print(IMAGE)

    process = subprocess.Popen(
        args=f"exiftool -Comment {IMAGE}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if stderr != b'':
        print(stderr)
    else:
        comm = stdout.decode('utf-8')
        comm = comm.split(":")[1].rstrip()
        process = subprocess.Popen(
            args=comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if stderr != b'':
            print(stderr)
        else:
            print(stdout.decode('utf-8'))


def main():


    global STEGANO, GET,  IMAGE

    opts, _ = getopt(sys.argv[1:], "s:g", [
                     "steg=", "get="])
    for key, value in opts:
        if key in ("-s", "--steg"):
            STEGANO = True
            IMAGE = value
        elif key in ("-g", "--get"):
            GET = True
            IMAGE = value
    if STEGANO:

        steg()
    elif GET:
        get()


if __name__ == '__main__':
    main()