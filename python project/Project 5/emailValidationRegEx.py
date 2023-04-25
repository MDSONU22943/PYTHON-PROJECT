#a-z  wscube@gmail.com
#0-9
#. _ times 1
# @ times 1
#. positon 3 or 4
# using regex

import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email Id:")

if re.search(email_condition,user_email):
    print("Right Email Id.")
else:
    print("Wrong Email Id.")