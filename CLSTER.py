
import requests
host = "https://www.pastebin.com/"    
        
str = 'zawew7y7'

def getBit(num, bit):
   return (num & 1 << bit) != 0

for i in range(0,2**len(str)):
   out = ""
   for bit in range(0,len(str)):
      if getBit(i,bit):
         out += str[bit].upper()
      else:
         out += str[bit].lower()

   r = requests.get(host + out)
   if r.ok:
        print(host + out)