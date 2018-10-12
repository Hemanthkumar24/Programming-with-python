import smtplib
import getpass
myemail=input("your emailid :")
password=getpass.getpass()
recemail=input("reciever's email id:")
#create SMTP session
s=smtplib.SMTP('smtp.gmail.com',587)
#start tls for security
s.starttls()
#aurhentication
s.login(myemail,password)
#message to be sent
message="Helo"
#sending th mail
s.sendmail(myemail,recemail,message)
#terminating the session
s.quit()