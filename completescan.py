#!/usr/bin/python3
import socket,sys,time
import argparse, sys,subprocess,os
parser = argparse.ArgumentParser(description="This tool")
parser.add_argument("-e",action="store_true",required=False)
a=parser.parse_args()
socket.setdefaulttimeout(0.01)
def sock_main(add,i):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((add, i))
            print(i,"open")
        except Exception as e:
            pass
        s=''
def total_range(ex):
    address = sys.argv[1]
    for i in range(15,25):
        if ex == address:
            pass 
        else:
            sock_main(address,i)
def multiple_range():
    for grp in sys.argv[1:]:
        print(grp)
        for i in range(0,23):
           sock_main(grp,i)

if 2 < len(sys.argv):
    pass

    # for grp in sys.argv[1:]:
    #     if [sys.argv[1]]:
        # elif sys.argv[1] and sys.argv[2]:
        #     print("multiple")
    multiple_range()
else:
    if a.e is True:
     total_range(a.e)


