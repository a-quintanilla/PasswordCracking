import sys, hashlib, os, bcrypt, itertools

mode = ""
attack = ""
pwfile = ""

def setMode(m):
    global mode
    mode = m

def setAttack(a):
    global attack
    attack = a

def checkMode(t):
    global mode
    if mode == t:
        return True
    else:
        return False

arguments = sys.argv[2:]
password = sys.argv[1]
if password in ['-p', '-m', '-s', '-b', '-d', '-B']:
    print("There's no password to crack!")
    quit()

for x in arguments:
    if x == '-p':
        setMode("PlainText")
    elif x == '-m':
        setMode("MD5")
    elif x == '-s':
        setMode("SHA-256")
    elif x == '-b':
        setMode("BCrypt")
    elif x == '-d':
        setAttack("Dictionary")
    elif x == '-B':
        setAttack("Brute Force")

if attack == "Brute Force" and mode != "PlainText":
    print("Sorry, you can only use Brute Force with PlainText :(")
    quit()
if len(mode) == 0:
    print("No mode found, choosing PlainText for you :)")
    setMode("PlainText")
if len(attack) == 0:
    print("No attack found, choosing Brute Force for you :)")
    setAttack("Brute Force")

if attack == "Dictionary":
    dict = open("10k-most-common.txt", "r")
    print("Checking the dictionary for you ;)")
    for line in dict:
        l = line.rstrip().encode('utf-8')
        if checkMode("MD5"):
            hashedLine = hashlib.md5()
            check = hashedLine.hexdigest()
        elif checkMode("SHA-256"):
            hashedLine = hashlib.sha256()
            check = hashedLine.hexdigest()
        elif checkMode("PlainText"):
            check = line.rstrip()
        elif checkMode("BCrypt"):
            th = password.rstrip().encode('utf-8')
            check = ""
            if bcrypt.checkpw(l, th):
                print("We found the password! It's " + line)
                quit()

        if check == password:
            print("We found the password! It's " + line)
            quit()
    print("We couldn't find the password :/")
    quit()

if attack == "Brute Force":
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cracked = ""
    for let in password:
        for x in alphabet:
            if x == let:
                cracked += x
    if cracked == password:
        print("We found the password! It's " + cracked)
        quit()
        
