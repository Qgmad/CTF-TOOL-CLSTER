import requests
#write the initial part of the link that you want to add before the test string in host:
host = "https://www.pastebin.com/"    
 
#Write the string you want to test for every possible combination of upper and lower case letters without changing their position: 
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
#All the validated and working links are shown on the display in live time.
