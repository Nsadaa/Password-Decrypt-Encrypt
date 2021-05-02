def encrypy_msg():

    c = input("Enter Your Message : ")
    e = []


    for i in c:
        e.append(ord(i)-1)

    print(f'Your Encrypted Values are : {e}')


def decrypt_msg():
    d = []
    while True:
        s = input("Enter Encrypted values press * at end : ")

        if s == "*":
            break
        else:
            d.append(int(s))

    for i in d:

        i += 1
        print(chr(i),end="")


print("WELCOME TO THE SECRET MASTER !")
option = input("WHAT DO YOU WANT ? IF DECRYPT PRESS D OR ELSE PRESS E : ")

while option == "D" or "E":

    if option == "D":
        decrypt_msg()
        break


    elif option == "E":
        encrypy_msg()
        break

    else:
        option = input("WHAT DO YOU WANT ? IF DECRYPT PRESS D OR ELSE PRESS E : ")
        continue


print("\nTHANK YOU !")
