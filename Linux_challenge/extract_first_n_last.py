

def check():
    second_nineth_char_strings = ""
    datafile = open('Linux_Challenge/Meta2/Password.txt')
    found = False
    for line in datafile:
        second_nineth_char_strings += (line[1]+line[8])
    datafile.close()
    return second_nineth_char_strings

def check_():
    second_nineth_char_strings = ""
    f = open("password.txt", "w")
    
    datafile = open('Linux_Challenge/Meta2/Password.txt')
    for line in datafile:
        second_nineth_char_strings = line[0 : 2 : ] + line[1 + 2 : :]
        second_nineth_char_strings = second_nineth_char_strings[0 : 2 : ] + second_nineth_char_strings[1 + 2 : :]
        f.write(second_nineth_char_strings)
    f.close()
    datafile.close()
    f.close()


if __name__ == "__main__":
    print(check())
    print(check().lower())
    print(check())
