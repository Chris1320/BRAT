Basic Remote Administration Tool (BRAT)
Copyright (C) 2018 :: Catayao56
================
This program is a basic Remote Administration Tool (RAT)
that allows you to execute commands remotely. This can be
used as a backdoor to any operating systems, as long as
the target machine has python 3 installed or the payload
is sent and executed to the target machine as a native code.
When using over WAN, both the attacker and the target machine
must have a stable internet connection. It is recommended to
compile the payload into executable binary format to hide the
code. Or else, your IP and port will be visible.

What's new?
------------------
1.Initial Release

Full Feature List
------------------------
1.Remote Administration Tool
      -Execute commands to a remote machine like cd, ls, etc.

2.Auto reconnection
      -The payload in the victim's side automatically restarts
      itself after a connection error occurs.

3.Server/Client Architecture
      -The Attacker is the server and the victim is the client.
      Because dynamic IPs are used by so many machines, it
      cannot start a session when the victim's machine has
      obtained his new IP. But if the attacker has a static IP,
      it doesn't matter if the victim's machine has Dynamic or
      Static IP.

TO-DO List
------------------------
1.More stable command-line interface.
2.Recieving of long output (more than 10,000 bytes).
      -When the attacker sends a command that outputs a long result,
      the attacker recieves only 10,000 bytes of the data. And the
      next command, instead of getting the output of the command
      from the victim, it sends the rest (10,001st byte and so on)
      of the previous command. So instead of getting the desired
      result, it delays the output.

License and Copying
-----------------------

-See LICENSE file.

Credits
------------------------
Catayao56 :: Developer


Requirements
------------------------
Server Side (Attacker):
      -Python 3
      -Internet Connection (for attacks over WAN)

Client Side (Victim):
      -Python 3 (if payload is not compile to executable binary)
      -Internet Connection (for attacks over WAN)


Installing & Running
------------------------
A.Linux

      $: apt update [1]
      $: apt install git python3 python3-dev [2]
      $: git clone https://github.com/Catayao56/BRAT.git [3]
      $: cd BRAT/src [4]
      $: chmod 755 BRAT.py [5]
      $: ./BRAT.py [6]

      [1] Update package information.
      [2] Install Git, Python 3, and Python 3-Dev.
      [3] Clone BRAT.
      [4] change directory to BRAT/src
      [5] change mode to executable.
      [6] Run BRAT.py

      [i] Remember to run as root!

B.Windows

      [i] Not yet tested on Windows!
