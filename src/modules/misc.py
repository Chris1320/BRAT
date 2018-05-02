#!/bin/python
# Coding=UTF-8

import os
import sys
import random

if sys.platform == 'linux' or sys.platform == 'darwin':
    # Colors with meanings
    CW = '\033[0m'     #  white     (normal)
    CR = '\033[31m'    #  red       (errors)
    CG = '\033[32m'    #  green     (main color)
    CY = '\033[33m'    #  yellow    (warnings)
    CB = '\033[34m'    #  blue      (highlights)
    CGR = '\033[37m'   #  gray      (questions)

    # Misc colors
    CP = '\033[35m'    #  purple
    CC = '\033[36m'    #  cyan

    # Font types
    FR = '\033[0m'     #  regular
    FB = '\033[1m'     #  bold
    FI = '\033[3m'     #  italic

else:
    # No color support on windows operating systems.
    CW = ''
    CR = ''
    CG = ''
    CY = ''
    CB = ''
    CGR = ''

    CP = ''
    CC = ''

    FR = ''
    FB = ''
    FI = ''

class programFunctions:
    COPYRIGHT = "Copyright(C) 2017-2018 by Shadow Team"

    def program_restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

    def clrscrn(self):
        try:
            platform = sys.platform
            if platform == 'linux':
                os.system('clear')

            elif platform == 'windows' or platform == 'nt':
                os.system('cls')

            else:
                os.system('clear')
                # DEV0001: Thinking of new generic clrscrn...
                """
                loop = 0
                while loop != 100:
                    print()
                    loop += 1
                """

        except KeyboardInterrupt:
            pass

    def pause(self, silent=False):
        try:
            """
            platform = sys.platform
            if platform == 'linux':
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')

            elif platform == 'windows':
                if silent is False:
                    os.system('pause')

                else:
                    os.sysem('pause > nul')

            else:
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')
            """

            if silent == True:
                input()

            else:
                input("Press enter to continue...")

        except KeyboardInterrupt:
            pass

    def error_except(self):
        try:
            loop = True
            while loop == True:
                quit = None
                ask = input(CB + FB + FI + 'Do you want to keep running? (y/n)> ' + CW + FR)
                ask = ask.lower()
                if ask == 'y':
                    loop = False
                    quit = False

                elif ask == 'n':
                    loop = False
                    quit = True

                else:
                    loop = True

            return quit

        except KeyboardInterrupt:
            pass

    def get_platform(self):
        result = sys.platform
        return result

    def cli_color_support(self):
        PLATFORM = self.get_platform()
        if PLATFORM == 'linux':
            return True

        elif PLATFORM == 'windows':
            return False

        else:
            # Just to be sure that we will not mess up everything.
            return False

    def is_windows(self):
        PLATFORM = self.get_platform()
        if PLATFORM == 'windows':
            return True

        else:
            return False

    def generate_session_id(self):
        session = random.randint(111111, 999999)
        return session
