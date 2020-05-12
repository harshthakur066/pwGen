import string
import random
import sys
import pyperclip
from math import log
from pyfiglet import Figlet

custom_ascii = Figlet(font='graffiti')
print(custom_ascii.renderText('pwGen'))


N = int(input("[+] Enter size of string --> "))
choice = input("[+] Obsfucate the passcode? [Y/n] ")
savef = input("[+] Do you want to save the file? [Y/n]")

   
if choice == 'n' or choice == 'N':
    pass
else:
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=N))
    res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')



if savef == 'n' or savef == 'N':
    print("[+] The generated random string --> " + str(res))
else:
    filename = input("[+] Input the Filename --> ")
    with open(filename, mode='w') as f:
        f.write(res)
        f.close()


ctoc = input("[+] Copy password to clipborad? [Y/n] ")
if ctoc == 'n' or ctoc == 'N':
    pass
else:
    pyperclip.copy(res)
    print("[+] Password copied to clipboard...")   

entropy = ((log(82)/log(2)) * len(res))

print ('')
print ('+------------------------------------+---------------------+')
print ('| Password                           | Entropy             |')
print ('+------------------------------------+---------------------+')
print (' %s                           %s                  ' % (res, entropy))



