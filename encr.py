from cryptography.fernet import Fernet
import os
import time
import random

def refresh():
    files = []
    for file in os.listdir():
        if file != "encr.py" and file != "key.key" and os.path.isfile(file):
            files.append(file)
    print(f"{len(files)} files in directory:")
    totalSize = 0
    totalUnit = "KB"
    for file in files:
        totalSize += os.path.getsize(file)
    totalSize = totalSize / 1024
    if totalSize >= 1024:
        totalUnit = "MB"
        totalSize = totalSize / 1024
    if totalSize >= 1024:
        totalUnit = "GB"
        totalSize = totalSize / 1024
    print(f"total size: {round(totalSize, 2)}{totalUnit}")
    return files

def generateKey(password):
    #whitespace or null password, generate 6 digit PIN
    if password == None or password.isspace() or password == "": 
        string = list()
        for x in range(6):
            string.append(str(random.randint(0, 9)))
        password = ''.join(string)

    if not os.path.exists("key.key"):
        print(f"key.key file generated with password {password}.\n")
        open("key.key", "wb").write(Fernet.generate_key()) 
        open("key.key", "a").write(f"\n{password}")
    else:
        print("key already exists in this directory.")

def modify(fileList, isEncrypting, password):

    #get the key from the key.key file
    key = None
    if not os.path.exists("key.key"):
        print("there's no key here.\n")
        return
    else:
        keyfile = open("key.key", "r").read().splitlines()
        if len(keyfile) != 2 or password != keyfile[1]:
            print("invalid input.\n")
            return
        key = keyfile[0]
    
    #mark timing, then print status
    TT = time.time()
    if isEncrypting:
        print("ENCRYPTING FILES\n")
    else:
        print("DECRYPTING FILES\n")

    #loop through the list of files
    count = 1
    for file in fileList:
        t = time.time()
        size = os.path.getsize(file) / 1024 #size in KB
        unit = "KB"
        # if size is more than 1024KB, use MB as units instead, divide by 1024
        if size >= 1024:
            unit = "MB"
            size = size / 1024
        # if size is more than 1024MB, use GB as units instead, divide by 1024
        if size >= 1024:
            unit = "GB"
            size = size / 1024
        # ^^ figuring out which unit to use and what number to display
        print(f"processing {file}")
        print(f"size: {round(size, 3)}{unit}")

        with open(file, "rb") as thefile: # open file, read binary mode
            contents = thefile.read() # read contents

        if isEncrypting:
            contents_modified = Fernet(key).encrypt(contents) # encrypt or decrypt contents using the key
        else:
            contents_modified = Fernet(key).decrypt(contents)

        with open(file, "wb") as thefile: # open file, write binary mode
            thefile.write(contents_modified) #write the modified contents into file

        if isEncrypting:
            os.rename(file, Fernet(key).encrypt(file.encode()))
        else:
            os.rename(file, Fernet(key).decrypt(file.encode()))
    
        print(f"files processed: {count}/{len(fileList)}")
        print(f"time taken: {round(time.time() - t, 4)} seconds\n")
        count += 1
    
    #calculating time, along with the units
    totalTime = time.time() - TT
    timeUnits = "seconds"
    if totalTime > 60:
        totalTime / 60
        timeUnits = "minutes"
    if totalTime > 60:
        totalTime / 60
        timeUnits = "hours"
    print(f"total time taken: {round(totalTime, 3)} {timeUnits}\n")

while(True):
    files = refresh()
    inp = input("\n>> ")
    print()
    if inp.startswith("encrypt"):
        password = inp[8::]
        modify(files, True, password)
        continue
    if inp.startswith("decrypt"):
        password = inp[8::]
        modify(files, False, password)
        continue
    if inp == "list files":
        print("these are the target files:")
        for file in files:
            print(file)
        print()
        continue
    if inp.startswith("get key"):
        passw = inp[8::]
        generateKey(passw)
        continue
    if inp == "exit":
        break
    print("invalid input.")