import os
from colorama import Fore, Back, Style

os.system("clear")

banner = print(Fore.BLUE+"""
  ██████   █████   ██▓        ███▄ ▄███▓ ▄▄▄       ██▓███  
▒██    ▒ ▒██▓  ██▒▓██▒       ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
░ ▓██▄   ▒██▒  ██░▒██░       ▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
  ▒   ██▒░██  █▀ ░▒██░       ▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
▒██████▒▒░▒███▒█▄ ░██████▒   ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░   ░  ░      ░  ▒   ▒▒ ░░▒ ░     
░  ░  ░     ░   ░   ░ ░      ░      ░     ░   ▒   ░░       
      ░      ░        ░  ░          ░         ░  ░         
                                                           
                        GitHub: https://github.com/xRiseStrqfe
                        Discord: https://discord.gg/heCDv6V        
               """)
print(banner)

url = input("Sql Açığı Aranan Site ----->")
level = input("Taramayı Ne Kadar Ayrıntıyla Yapalım----->")
risk = input("Risk Seviyesini Belirleyin----->")


os.system("clear")
os.system("sqlmap -u "+url+"--dbs --level="+level+" --risk="+risk+" --batch -randomagent")

print("Sql Injection Açıkğı Araması Bitmiştir, Bizi Tercih Ettiğiniz İçin Teşekkürler.")
print("A xRiseStrqfe Script")