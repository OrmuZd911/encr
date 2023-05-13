from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os
import time
import random

currentDirectory = os.getcwd()

def browseFiles():
    root = tk.Tk()
    root.geometry("10x10")
    filepath = filedialog.askopenfilename(title='select file')
    root.destroy()
    if filepath[-4:] != '.key':
        print("unsupported file type.\n") # key not .key extension
        return None
    file = open(filepath, 'r')
    conf = input("confirm password: ")
    filelines = file.readlines()
    if conf == filelines[1]:
        print()
        return filelines[0]
    else:
        print("unable to retrieve key.")
        return None
    
def refresh():
    files = []
    for file in os.listdir(currentDirectory):
        if file != os.path.basename(__file__) and file != "key.key" and os.path.isfile(currentDirectory + "/" + file) and file[-4:] != ".ini":
            files.append(file)
    print(f"Target directory: {currentDirectory}")
    print(f"{len(files)} files in directory:")
    totalSize = 0
    totalUnit = "KB"
    for file in files:
        totalSize += os.path.getsize(currentDirectory + "/" + file)
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
    if password == "select key":
        print("invalid password.\n")
        return
    #whitespace or null password, generate 6 digit PIN
    if password == None or password.isspace() or password == "": 
        string = list()
        for x in range(6):
            string.append(str(random.randint(0, 9)))
        password = ''.join(string)
    if not os.path.exists(currentDirectory + "/" + "key.key"):
        print(f"key.key file generated with password {password}.\n")
        open(currentDirectory + "/" + "key.key", "wb").write(Fernet.generate_key()) 
        open(currentDirectory + "/" + "key.key", "a").write(f"\n{password}")
    else:
        print("key.key already exists in this directory.\n")

def modify(fileList, isEncrypting, password):
    #get the key from the key.key file
    if(password != 'select key'):
        key = None
        if not os.path.exists(currentDirectory + "/" + "key.key"):
            print("there's no key here.\n")
            return
        else:
            keyfile = open("key.key", "r").read().splitlines()
            if len(keyfile) != 2 or password != keyfile[1]:
                print("invalid input.\n")
                return
            key = keyfile[0]
    else:
        key = browseFiles()
        if key == None:
            return  

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
        size = os.path.getsize(currentDirectory + "/" + file) / 1024 #size in KB
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

        with open(currentDirectory + "/" + file, "rb") as thefile: # open file, read binary mode
            contents = thefile.read() # read contents

        if isEncrypting:
            contents_modified = Fernet(key).encrypt(contents) # encrypt or decrypt contents using the key
        else:
            contents_modified = Fernet(key).decrypt(contents)

        with open(currentDirectory + "/" + file, "wb") as thefile: # open file, write binary mode
            thefile.write(contents_modified) #write the modified contents into file

        if isEncrypting:
            os.rename(currentDirectory + "/" + file, currentDirectory + "/" + Fernet(key).encrypt(file.encode()).decode())
        else:
            os.rename(currentDirectory + "/" + file, currentDirectory + "/" + Fernet(key).decrypt(file.encode()).decode())

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
        print("These are the target files:")
        for file in files:
            print(file)
        print()
        continue
    if inp.startswith("get key"):
        passw = inp[8::]
        generateKey(passw)
        continue
    if inp == "change dir":
        root = tk.Tk()
        root.geometry("10x10")
        currentDirectory = filedialog.askdirectory(title='select directory')
        root.destroy()
        continue
    if inp == "del keys":
        c = 0
        for file in os.listdir(currentDirectory):
            if file[-4::] == ".key":
                os.remove(currentDirectory + "/" + file)
                c += 1
        print(f"Deleted {c} keys in this directory.\n")
        continue
    if inp == "del all":
        c = len(files)
        for file in files:
            os.remove(currentDirectory + "/" + file)
        print(f"Deleted {c} files in this directory.\n")
    if inp == "del self":
        os.remove(__file__)
        break
    if inp == "x":
        break
    print("invalid input.\n")
