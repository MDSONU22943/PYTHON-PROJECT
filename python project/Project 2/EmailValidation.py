# check email validation in standard email

email=input("Enter your Email:")    #g@g.in,wscube@gmail.com
space,uppercase,specialChracter=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        space=1
                    elif i.isalpha():
                        if i==i.upper():
                            uppercase=1 
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:  #for special character
                        specialChracter=1
                if space==1 or uppercase==1 or specialChracter==1:
                    print("Wrong Email 5")   # there is space,upper character alphabet or special character(other than '_','.','@') this.
                else:
                    print("Your Entered Email is Right")   #finally our email is right 
            else:
                print("Wrong Email 4") # there is no . symbol in -3 or -4 index position in our email or present in both in indexes(-3or-4)
        else:
            print("Wrong Email 3")   #there is no @ symbol in given email or there is more than 1 @ symbol in given email
    else:
        print("Wrong Email 2") #starting symbol is not alphabet
else:
    print("Wrong Email 1")  #missing length
