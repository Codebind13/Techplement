import string
import random

length=int(input("enter the size of the password"));

print(''' Choose character :
      1.Letters
      2.Digits
      3.Special Characters
      4.Exit''')
charList= ""
while(True):
    choice=int(input("pick a number"))
    if(choice==1):
        print('''Please pick the type of alphabet:
        1.Uppercase letter
        2.Lowercase letter
        3.Both''')
        while(True):
            ch=int(input("pick the type of alphabet: "))
            if(ch==1):
                charList += string.ascii_uppercase
                break
            elif(ch==2):
                charList += string.ascii_lowercase
                break
            elif(ch==3):
                charList += string.ascii_letters
                break
    elif(choice == 2):
        charList += string.digits
    elif(choice == 3):
        charList += string.punctuation
    elif(choice==4):
        break
    else:
        print("Invalid Option")
password= []
for i in range(length):
    randomch=random.choice(charList)
    password.append(randomch)

print("the generated passord is "+ "".join(password))