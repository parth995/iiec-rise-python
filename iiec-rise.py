import os
import platform
#import pyttsx3

print("#############################################################")
print('Hey ' + os.getlogin() + '!! Welcome to IIEC Rise Python challenge world !!!!!')
print('To fetch the OS & resources details, network checks, play with files and dirs')
print("#############################################################")

print('press 1: if you want to chat with bot : ')
print('press 2: if you want to drive through menu :', end='')
op = int(input())
while True:
    if(op == 1):
        print("enter the message please : ", end='')
        txt = input()
        if(("dns lookup" in txt) or ("dns query" in txt) or ("perform dns" in txt) or ("dns resolution" in txt) or ("dns" in txt)):
            print("enter hostname to lookup : ", end='')
            a1 = input()
            res = os.system("nslookup " + a1)
        elif("ping" in txt):
            print("enter hostname to ping : ", end='')
            a2 = input()
            res = os.system("ping " + a2)
        elif(("install tool" in txt) or ("install software" in txt) or ("application install" in txt) or ("add new software" in txt) or ("new tool" in txt)):
            print("enter path to install new application :", end='')
            fpath = input()
            cpath = os.chdir(fpath)
            print("changed directory is : " + os.getcwd())
            print('enter application name to be installed :', end='')
            aname = input()
            if(aname):
                os.system(aname)
            else:
                print('invalid name')
        elif(("print OS details" in txt) or ("fetch OS details" in txt) or ("OS and user details" in txt) or ("OS details" in txt)):
            print("OS is : " + platform.system())
            print("USer logged in is : " + os.getlogin())
            print("CPU Count is : " + str(os.cpu_count()))
        elif("quit" in txt or "bye" in txt or "terminate" in txt or "exit" in txt):
            exit()


    if(op == 2):
        print("#############################################################")
        print('Hey ' + os.getlogin() + '!! Welcome to IIEC Rise Python challenge world !!!!!')
        print('press 1: to fetch the OS & resources details')
        print('press 2: to explore network bot')
        print('press 3: to install any software (setup must be in .exe format only)')
        print('press 4: play with files and directories')
        print('press 5: quit to exit')
        print("#############################################################")

        print('enter your choice: ', end='')
        c = int(input())
        if(c == 1):
            print("OS is : " + platform.system())
            print("USer logged in is : " + os.getlogin())
            print("CPU Count is : " + str(os.cpu_count()))
            #print(os.getuid())
            #os.system("chrome")


        if(c == 2):
            print('press 1: for ping check')
            print('press 2: for nslookup check')
            print('press 3: quit')
            
            print('######################################')
            print('enter your choice for network bot: ', end='')
            ch = int(input())
            if(ch == 1):
                print("enter IP or hostname to check ping: ", end='')
                ip = input()
                resp = os.system("ping    " + ip)
                if(resp == 0):
                    print("Host is up")
                else:
                    print("down or unreachable or not valid FQDN")
                    print()
                # file = open('pingout.txt','w')
                # file.write(resp)
                # file.close()
                # r = open('pingout.txt','r')
                # if("0%" in r.read()):
                #     print("its up")
                # elif(("timed out" in r.read()) or ("host unreachable" in r.read()) or ("ttl expired in transit" in r.read())):
                #     print("There seems to be an issue reaching host")
                # elif(("unknown host" in r.read()) or ("could not find host") in r.read()):
                #     print("Invalid host")
            elif(ch == 2):
                print("enter hostname or IP to perform DNS lookup: ", end='')
                hn = input()
                res = os.system("nslookup " + hn)
            elif(ch == 3):
                exit()


        if(c == 3):
            print("Does the software already exists ? ")
            curfilepath = os.getcwd()
            print('current working dir is :' + curfilepath)
            print('Enter file/application path to install')
            newfilepath = input()
            chgfilepath = os.chdir(newfilepath)
            print('Changed directory is:' + os.getcwd())
            print('Below are files present in directory : ')
            print(os.listdir(chgfilepath))
            print('Enter application name to be installed :', end='')
            appname = input()
            if(appname):
                os.system(appname)
            else:
                print('invalid name')
        

        if(c == 4):
            print('Press 1: to create directories')
            os.makedirs(input())


        if(c == 5):
            exit()




            