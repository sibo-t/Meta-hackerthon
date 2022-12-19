

def check():
    instagram_followers = 0
    datafile = open('Linux_Challenge/Meta4/Profile_1.txt')
    found = False
    for line in datafile:
        if "instagram followers" in line:
            instagram_followers+=int(line.split()[2])
    datafile.close()
    return instagram_followers

def check_profile2():
    instagram_followers = 0
    datafile = open('Linux_Challenge/Meta8/Profile_2.txt')
    found = False
    for line in datafile:
        if "instagram followers" in line:
            instagram_followers+=int(line.split()[2])
    datafile.close()
    return instagram_followers

if __name__ == "__main__":
    print(check()-check_profile2())