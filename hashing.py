import hashlib as hlib
testhash = 0


def hashing_fun(passwrd_hash):
    global testhash
    testhash = hlib.sha256(passwrd_hash.encode())
    print("Hash output: ",testhash.hexdigest())
    
def main():
    passwrd_hash = input("Please enter your password: ")
    hashing_fun(passwrd_hash) 
    users_choice = input("Hey do you wish to see if you have the Correct password? Y/N: ").upper()
    if(users_choice == "Y"):
        hash_check()

def hash_check():
    users_pass = input("enter you pass word to test.")
    users_hash = hlib.sha256(users_pass.encode())
    if(users_hash.hexdigest() == testhash.hexdigest()):
        print("Password confirmed")
        print("second password: ",users_hash.hexdigest())
        print("first password: ",testhash.hexdigest())
    else:
        print("Password is not the same")
        print("second password: ",users_hash.hexdigest())
        print("first password:  ",testhash.hexdigest())
        
main()