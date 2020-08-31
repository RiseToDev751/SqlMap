import os

os.system("clear")

banner = """
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
"""

print(banner)

url = input("Sql Açığı Aranan Site ----->")

os.system("clear")
os.system("sqlmap -u"+url+"--dbs")

print("Sql Injection Açıkğı Araması Bitmiştir, Bizi Tercih Ettiğiniz İçin Teşekkürler.")
print("A xRiseStrqfe Script")