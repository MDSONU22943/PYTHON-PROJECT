import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("mdsonu22943@gmail.com","sonu@123")
subject="test python"
body="I Love Python"
message="subject:{}\n\n{}".format(subject,body)
listadd=["junaidjdsiddiqui212gmail.com"]
ob.sendmail("mdsonu22943@gmail.com",listadd,message)
print("sent mail")
ob.quit()