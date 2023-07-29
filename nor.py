#Decoded By Dex : @k06bot  



foo = False
if foo:
    pass
import pyfiglet
import os
import sys
import subprocess
import webbrowser
import requests
import random
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[1;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
insta = 'sgwiwphwfczzbnxmskagwppqdyu91636389262791'
ajw = '_.'
B = '\x1b[1;30m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
Bl = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
E = '\x1b[0;90m'
ajaj = pyfiglet.figlet_format(' N O E R A ')
print(F + ajaj)
print('………………………………………')


import requests 
import random 
import webbrowser
webbrowser.open('https://t.me/llll7l3')
import datetime
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="_._._._._."
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
#------------------logo---------------------#
#-------------------------start code ---------------------------#
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(W + f'''  {X} NO {A}{user} ''')
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(W + f''' {F} NO {C}{user} ''')
    else:
        email=0
        print(W + f''' {C} Yes  {F}{user} ''')
        email+=1
        god=f"""\n\n Yes : {user}\n ═══════════════════\n user : Instagram\n═══════════════════\nBY: @Xcrr2r1 𓂐 @llll7l3"""

        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="shiwwopquwrwisvczjxogwwipqqgsgdodbxf926292529106hdisg_.iehgdhdhh"
    while True:
           v1 = str(''.join((random.choice(insta) for i in range(1))))
           v2 = str(''.join((random.choice(insta) for i in range(1))))
           v3 = str(''.join((random.choice(insta) for i in range(1))))
           v4 = str(''.join((random.choice(insta) for i in range(1))))
           v5 = str(''.join((random.choice(all) for i in range(1))))
           user1 = (v5+v1+v2+v3+v4)
           user2 = (v1+v5+v2+v3+v4)
           user3 = (v1+v2+v5+v3+v4)
           user4 = (v1+v2+v3+v5+v4)
           hamo010 = (user1, user2, user3, user4)
           user = random.choice(hamo010)
           instaa(user)
id=input(f'''{F} ID TELE →{W}''')
print('………………………………………')
token=input(f'''{Bl} TOKEN BOT →{P}''')
print('………………………………………')
users()
