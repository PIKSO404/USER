
#coding/utf/
#created/by/MAFIA UA
import os
import random
def clear():
    os.system('clear')
    print(logo)
logo=(f"""\033[1;37m
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m.88b  d88.  .d8b.  d88888b d888888b  .d8b.  
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88'YbdP`88 d8' `8b 88'       `88'   d8' `8b 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88ooo88 88ooo      88    88ooo88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88~~~88 88~~~      88    88~~~88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88   88 88        .88.   88   88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYP  YP  YP YP   YP YP      Y888888P YP   YP 
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mFACEBOOK: ANIS M.SCHIAPARELLI 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mGithub  : PIKSO404
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYOUR UA : USERAGENT
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mFacebook: ANIS M.SCHIAPARELLI 
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mCloning ids Saved in MAFIA folder
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
def linex():
    print('\033[1;32m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
clear()
print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYOUR UA \033[97;1m[\033[1;32mUSERAGENT\033[97;1m] \033[1;32mLIST HERE\n\033[1;97m==================================================')
for i in range(100):
        model_build = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix", "Oppo", "Qmobile"])
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = 'null'
        fban = random.choice(["FB4A"])
        fbpn = random.choice(["com.facebook.katana"])
        fbbd = 'lge'
        user_agent = f"\033[1;32m[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/lge;FBBD/{fbbd};FBPN/{fbpn};FBDV/LGE;FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
print(user_agent)
            
