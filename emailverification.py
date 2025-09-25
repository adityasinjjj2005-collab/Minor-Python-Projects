Email = input("Enter your email: ")
k = 0
if len(Email) >= 6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@") == 1):
            if (Email[-4] == ".") ^ (Email[-3] == "."):
                for i in Email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i in ['_', '.', '@']:
                        continue
                    else:
                        k = 1
                if k == 1:
                    print("wrong email5")
                else:
                    print("Email is valid")
            else:
                print("email is wrong 4")
        else:
            print("email is wrong 3")
    else:
        print("email is wrong 2")
else:
    print("email is wrong 1")