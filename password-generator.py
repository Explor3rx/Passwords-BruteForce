#!usr/bin/python3
def main():
        menu()



def menu():
        print ('''############################################################
#                          Expl0r3r	                   #
#           Python spear generator passwords               #
############################################################''')
        inputs()




def save_file(passwords):
        filename = str(input("Password file name:"))
        with open(filename, "w") as filehandle:
                for list in passwords:
                        filehandle.write("{}\n".format(list))


def inputs():
        name = str(input("Enter First Name: "))
        name2 = str(input("Enter Nick/Second Name: "))
        sur = str(input("Enter Last Name: "))
        child = str(input("Enter Child name: "))
        pet = str(input("Enter pet name: "))
        phone = str(input("Enter Phone Number(0501234567): "))
        idn = str(input("Enter ID Number: "))
        birthday = str(input("Enter birthday date(DD/MM/YYYY): "))
        additionally = str(input("Enter Something in addition: "))
        print ("\n")
        dd = str(birthday[0:2])
        mm = str(birthday[3:5])
        yyyy = str(birthday[6:10])
        
        text_input = [name, name2, sur, child, pet, additionally]
        numbers_input = [idn, dd, mm, yyyy, dd+mm, dd+mm+yyyy]

        while(True):
                passwords = []
                text_input_cap = [i.capitalize() for i in text_input]
                for i in text_input:
                        passwords.append(i)
                        for x in range(6):
                                passwords.append(i+text_input[x])
                                passwords.append(i+numbers_input[x])
                                for c in range(33, 48):
                                        passwords.append(chr(c)+i)
                                        
                for i in text_input_cap:
                        passwords.append(i)
                        for x in range(6):
                                passwords.append(i+text_input_cap[x])
                                passwords.append(i+text_input[x])
                                passwords.append(i+numbers_input[x])
                        for c in range(33, 48):
                                passwords.append(chr(c)+i)
                                
                for i in numbers_input:
                        passwords.append(i)
                        print (passwords)
                        print ("Number of Passwords: ", len(passwords))
                        basicpass = str(input("Do you want to add the 10,000 most common passwords(123456, password,  etc) ? press y/n: ")) 
                        if basicpass == "y":
                                FileRead = open("passwords.txt", 'r')
                                text = FileRead.read()
                                passwords.append(text)
                                FileRead.close()
                                print ("After the basic passwords: ", len(passwords))
                        break
                save_file(passwords)
                break


if __name__ == "__main__":
        main()
