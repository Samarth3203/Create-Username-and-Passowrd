# This is a program of password matching and criteria of password
#with out using loop

print('''a. The password should be at of 4 characters long. \nb. The first two character must be from English letter alphabet. \nc. The password must contain a combination of uppercase letters, lowercase letters. \nd. Third character of the password must be a digit.\ne. Fourth character must be among the symbol "_" or "-"or"#"."''')
password_1=input("Enter the Password :") # this is criteria of passowrd

password_2=input("Re-enter the Password:")

if password_1==password_2: #matching password
    if len(password_1) <= 4: # check length of password
        if password_1[:2].isalpha(): #check First two character is english alphabet
           if (((password_1[0:1].isupper() or password_1[1:2].isupper()) and (password_1[0:1].islower() or password_1[1:2].islower()))): #it is checking combination of upper case and lowwer case
               if password_1[2:3].isdigit():  # it is checking 3rd character must be digit
                   if ((password_1[3:4]=="_")or(password_1[3:4]=="-")or(password_1[3:4]=="#")):  # it is for some symbols 
                       print("Valid Password")
                   else:
                       print("""Fourth character must be among the symbol"_","-","#" """)   
               else:
                   print("Third Character must be a digit")   
           else:
               print("Password must contain a combination of uppercase and lowercase character")
        else:
            print("First 2 character must be alphabet")    
    else :
        print("Password must be 4 character long")
else:
    print("Password doesn't Match")    

