import random,string
def password_generator(len):
    digits="9876543210"
    specialsymbol="@#$"
    tool=string.ascii_letters+digits+specialsymbol
    generatepassword1="".join(random.choices(tool,k=len))
    print(f"Generated password : {generatepassword1}")

password_generator(int(input("Enter the length of the password :")))