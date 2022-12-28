#!/usr/bin/python3
import socket,sys,time
import argparse, sys,subprocess,os
global newval
# parser = argparse.ArgumentParser(description="This tool")
# parser.add_argument("-e",action="store_true",required=False)
# a=parser.parse_args()
socket.setdefaulttimeout(0.01)
def sock_main(add,i,exe):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if exe !=0:    
            newexe=exe.split(".")
            newadd = newval[:newval.rfind('.')+1] + str(add)
            # print(newadd,"lookhere")
            if  int(newexe[3])==int(add):
                pass
                # print(newadd,"excluded")
            else:
                try:
                    # print(newadd,i)            
                    s.connect((newadd, i))
                    print(newadd,i,"open")
                except Exception as e:
                    pass
        else:  
            try:
                # print(add,i)            
                s.connect((add, i))
                print(add,"open",i)
            except Exception as e:
                pass 
        s=''
def total_range():
    address = sys.argv[1]
    for i in range(15,25):
        # if ex == address: 
        #     pass 
        # else:
        sock_main(address,i,0)
def multiple_range():
    for grp in sys.argv[1:]:
        if "-e" in sys.argv[1:]:
            pass
        else:
            # print(grp)
            for i in range(15,25):
               sock_main(grp,i,0)
def define_range(add,rg,exe1):
    for t in range(15,25):
        val1=rg.split("-")
        newrg=val1[0].split(".")
        for i in range(int(newrg[3]),int(val1[1])+1):
            # print(i)
            if exe1 !=0:
                sock_main(i,t,exe1)
            else:
                newadd1 = newval[:newval.rfind('.')+1] + str(i)
                # print(newadd1,t)
                sock_main(newadd1,t,0)
def portfunc(ipa,prt):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:            
        s.connect((ipa, prt))
        print(ipa,"open",prt)
    except Exception as e:
        print(ipa,"closed",prt)
        pass
    s=''
if "-" in sys.argv[1]:
    # print(sys.argv[1])
    val1=sys.argv[1].split("-")
    # print(val1)
    # print(len(sys.argv[1:]))
    if len(sys.argv[1:]) > 2:
        if "-e" in sys.argv[2]:
            # print(sys.argv[3])
            newval=val1[0]
            define_range(val1[0],sys.argv[1],sys.argv[3])
    else:
        newval=val1[0]
        # print(val1[0],val1[1])
        define_range(val1[0],sys.argv[1],0)
elif len(sys.argv[1:]) > 2: 
    if "-p" in sys.argv[2]:
        if "," in sys.argv[3]:
            prt=sys.argv[3].split(",")
            for i in prt:
                portfunc(sys.argv[1],int(i))
        elif "-" in sys.argv[3]:
            prt=sys.argv[3].split("-")
            # print(prt[0],prt[1])
            for i in range(int(prt[0]),int(prt[1])+1):
                portfunc(sys.argv[1],int(i))
        else:
            portfunc(sys.argv[1],int(sys.argv[3]))
elif not "-" in sys.argv[1]:
    multiple_range()
else:
     total_range()
# else:
#     if a.e is True:
#      total_range(a.e)


