import requests
import os
import base64


ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
vmess_file = os.path.join(ptt, 'Splitted-By-Protocol/vmess.txt')
vless_file = os.path.join(ptt, 'Splitted-By-Protocol/vless.txt')
trojan_file = os.path.join(ptt, 'Splitted-By-Protocol/trojan.txt')
ss_file = os.path.join(ptt, 'Splitted-By-Protocol/ss.txt')
ssr_file = os.path.join(ptt, 'Splitted-By-Protocol/ssr.txt')
tuic_file = os.path.join(ptt, 'Splitted-By-Protocol/tuic.txt')
hysteria_file = os.path.join(ptt, 'Splitted-By-Protocol/hysteria.txt')
hysteria2_file = os.path.join(ptt, 'Splitted-By-Protocol/hysteria2.txt')

open(vmess_file, "w").close()
open(vless_file, "w").close()
open(trojan_file, "w").close()
open(ss_file, "w").close()
open(ssr_file, "w").close()
open(tuic_file, "w").close()
open(hysteria_file, "w").close()
open(hysteria2_file, "w").close()

vless = ""
trojan = ""
ss = ""
ssr = ""
tuic = ""
hysteria = ""
hysteria2 = ""

response = requests.get("https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt").text
for config in response.splitlines():
    if config.startswith("vmess"):
        open(vmess_file, "a").write(config + "\n")     
    if config.startswith("vless"):
        vless += config + "\n"  
    if config.startswith("trojan"):
        trojan += config + "\n"   
    if config.startswith("ss"):   
        ss += config + "\n"
    if config.startswith("ssr"):
        ssr += config + "\n"
    if config.startswith("tuic"):
        tuic += config + "\n"
    if config.startswith("hysteria"):
        hysteria += config + "\n"
    if config.startswith("hysteria2"):
        hysteria2 += config + "\n"
 
open(vless_file, "w").write(base64.b64encode(vless.encode("utf-8")).decode("utf-8"))  
open(trojan_file, "w").write(base64.b64encode(trojan.encode("utf-8")).decode("utf-8"))  
open(ss_file, "w").write(base64.b64encode(ss.encode("utf-8")).decode("utf-8"))  
open(ssr_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))
open(tuic_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))
open(hysteria_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))
open(hysteria2_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))


