import random
import string
def Password_Genrator(length):
    all_char = string.ascii_uppercase+string.digits+string.punctuation
    Password = ''.join(random.choice(all_char) for _ in range(length))
    return Password
print("=====Password Genrator=====")
try:
    length = int(input("Enter your password length:"))
    Password = Password_Genrator(length)
    print("The Genrated Password is:",Password)
except:
    print("Please enter invaild number") 
