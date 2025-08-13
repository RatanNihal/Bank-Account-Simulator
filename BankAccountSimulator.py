import getpass
import dataofusernames
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_data():
    with open("dataofusernames.py", "w") as f:
        f.write(f"data = {repr(dataofusernames.data)}\n")


def menu(username):
    while True:
        print("bank menu")
        print("1.check bank balance:")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.quit")
        choice = int(input("enter the choice number:"))
        if choice==1:
            print("your bank balance is :",dataofusernames.data[username][1],"₹")
        
        elif choice==2:
            diposit=int(input("how many do you want to diposit your money:"))
            (dataofusernames.data[username][1])=(dataofusernames.data[username][1])+diposit
            save_data()
            print(f"you have diposited {diposit}₹ money.\nnow in your bank account has {dataofusernames.data[username][1]}₹.")
        
        elif choice==3:
            if (dataofusernames.data[username][1])==0:
                print("you cannot withdraw your money.\nbecause in your bank account has", (dataofusernames.data[username][1]),"₹.")
            
            else:
                withdraw=int(input("how many do you want to withdraw your money:"))
                if withdraw > dataofusernames.data[username][1]:
                    print("You cannot withdraw more than your balance.")
                else:
                    dataofusernames.data[username][1]=(dataofusernames.data[username][1])-withdraw
                    save_data()
                    print(f"you have withdraw {withdraw}₹ money from your bank account.\nnow in your bank account has left {dataofusernames.data[username][1]}₹.")
                
        elif choice==4:
            print("thank you to using this program")
            exit()
        else:
            print("invalid input.\nenter choice number between 1 to 4 only.\ntry again.")
        

def main ():
    while True:
        print("\nwelcome to the bank")
        print("1.signup\n2.login\n3.quit")
        choice=int(input("enter your choice :"))
        if choice==1:
            signup()
        elif choice==2:
            login()
        elif choice==3:
            print("Good bye")
            break
        else:
            print("invalid input.\nenter choice number between 1 to 4 only.\ntry again.")
            


def login():
    chance=3
    while chance>0:
        username=input("enter your username:")
        password=getpass.getpass("enter password:")
        hashed_password = hash_password(password)
        if username in dataofusernames.data and dataofusernames.data[username][0]==hashed_password :
            print(f"you are login.\nwelcome {username}")
            menu(username)
        else:
            chance-=1
            if chance!=0:
                print(f"you have entered wrong username or password.\nyou have {chance} chances to login.\ntry again.")
                
            else:
                print("you have entered wrong password many times.\nyour account is locked")
            



def signup():
    chance=3
    while chance>0:
        username=input("enter your new username:")
        if username in dataofusernames.data:
            print("This username already exists. Please choose another one.")
            continue
        password=getpass.getpass("enter your new password:")
        verify_password=getpass.getpass("verify your password:")
        if password==verify_password:
            hashed_password = hash_password(password)
            dataofusernames.data[username]=[hashed_password,0]
            save_data()
            print(f"you have created your new bank account.\nwelcome {username}")
            menu(username)
        else:
            chance-=1
            if chance!=0:
                print(f"your password not matches to verify password.\nyou have {chance} chances to signup.\ntry again.")
                
            else:
                print("you have entered wrong password many times.\nyour account is locked")

main()