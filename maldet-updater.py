#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Maldet Scanner Signature Schedule Update Tool.
Author: DarkRix.
Signature Update Schedule: 0:00, 07:00, 12:00, 19:00
'''

import subprocess
from datetime import datetime
from time import sleep

Anker = ['0'] # Default value

while True:
    if datetime.now().second == 0: # Wait until zero seconds.
        while True:
            try:
                if Anker[0] == '0' and datetime.now().hour == 0: # 0:00
                    subprocess.run('/usr/local/sbin/maldet --update', shell=True)
                    Anker[0] = '1'
                elif Anker[0] == '0' and datetime.now().hour == 7: # 07:00
                    subprocess.run('/usr/local/sbin/maldet --update', shell=True)
                    Anker[0] = '1'
                elif Anker[0] == '0' and datetime.now().hour == 12: # 12:00
                    subprocess.run('/usr/local/sbin/maldet --update', shell=True)
                    Anker[0] = '1'
                elif Anker[0] == '0' and datetime.now().hour == 19: # 19:00
                    subprocess.run('/usr/local/sbin/maldet --update', shell=True)
                    Anker[0] = '1'
                else:
                    if Anker[0] == '1' and datetime.now().hour == 0:
                        sleep(60)
                    elif Anker[0] == '1' and datetime.now().hour == 7:
                        sleep(60)
                    elif Anker[0] == '1' and datetime.now().hour == 12:
                        sleep(60)
                    elif Anker[0] == '1' and datetime.now().hour == 19:
                        sleep(60)
                    else:
                        Anker[0] = '0'
                        sleep(60)
            except KeyboardInterrupt:
                break
        break
    else:
        sleep(1)
