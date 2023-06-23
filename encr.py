from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk
import os
import time
import random
import sys
from colorama import Fore, Style
import colorama
colorama.init()

print(
    """
     ___           ___           ___           ___     
    /\  \         /\__\         /\  \         /\  \    
   /::\  \       /::|  |       /::\  \       /::\  \   
  /:/\:\  \     /:|:|  |      /:/\:\  \     /:/\:\  \  
 /::\ \:\  \   /:/|:|  |__   /:/  \:\  \   /::\ \:\  \ 
/:/\:\ \:\__\ /:/ |:| /\__\ /:/__/ \:\__\ /:/\:\ \:\__\\
\:\ \:\ \/__/ \/__|:|/:/  / \:\  \  \/__/ \/_|::\/:/  /
 \:\ \:\__\       |:/:/  /   \:\  \          |:|::/  / 
  \:\ \/__/       |::/  /     \:\  \         |:|\/__/  
   \:\__\         /:/  /       \:\__\        |:|  |    
    \/__/         \/__/         \/__/         \|__|  

version 1.0
Made by Dimas Rizky
https://github.com/desolaterobot/encr
    """
)

currentDirectory = os.getcwd()
globalKey = "PjUYNENTBSGja15yQdPSzwNls-PKBWPRBrHDyxCdsFY="

def refresh():
    files = []
    for file in os.listdir(currentDirectory):
        #does not allow encr.files, key.key files, 
        if not file.startswith(os.path.basename(__file__)[:-2]) and not file.endswith(".key") and os.path.isfile(currentDirectory + "/" + file) and file[-4:] != ".ini":
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
        open(currentDirectory + "/" + "key.key", "wb").write(Fernet.generate_key()) 
        open(currentDirectory + "/" + "key.key", "a").write(f"\n{password}")
        keycontents = open(currentDirectory + "/" + "key.key", "rb").read()
        modifiedContents = Fernet(globalKey).encrypt(keycontents)
        open(currentDirectory + "/" + "key.key", "wb").write(modifiedContents)
        print(f"key.key file generated with password {password}.\n")
    else:
        print(".key file already exists in this directory.\n")

def readKey(address):
    contents = open(address, "rb").read()
    decrContents = Fernet(globalKey).decrypt(contents)
    return decrContents.decode().splitlines()

def browseFiles():
    root = tk.Tk()
    root.geometry("10x10")
    filepath = filedialog.askopenfilename(title='select key file')
    root.destroy()
    if filepath[-4:] != '.key':
        print("unsupported file type.\n") # key not .key extension
        return None
    keyfile = readKey(filepath)
    conf = input("confirm password: ")
    if conf == keyfile[1]:
        print()
        return keyfile[0]
    else:
        print("unable to retrieve key.\n")
        return None
    
def keyName():
    for file in os.listdir(currentDirectory):
        if(file.endswith('.key')):
            return file
    return "[]"

def modify(fileList, isEncrypting, password):
    #get the key from the key.key file
    if(password != 'select key'):
        key = None
        if not os.path.exists(currentDirectory + "/" + keyName()):
            print("there's no key here.\n")
            return
        else:
            #key exists!
            keyfile = readKey(currentDirectory + "/" + keyName())
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
            try:    
                contents_modified = Fernet(key).encrypt(contents) # encrypt or decrypt contents using the key
            except:
                print(Fore.RED + "DATA ENCRYPTION ERROR.\n" + Style.RESET_ALL)
                continue
        else:
            try:
                contents_modified = Fernet(key).decrypt(contents)
            except:
                print(Fore.RED + "DATA DECRYPTION ERROR.\n" + Style.RESET_ALL)
                continue

        with open(currentDirectory + "/" + file, "wb") as thefile: # open file, write binary mode
            thefile.write(contents_modified) #write the modified contents into file

        if isEncrypting:
            try:
                os.rename(currentDirectory + "/" + file, currentDirectory + "/" + Fernet(key).encrypt(file.encode()).decode())
            except:
                print(Fore.RED + "NAME ENCRYPTION ERROR.\n" + Style.RESET_ALL)
                continue
        else:
            try:
                os.rename(currentDirectory + "/" + file, currentDirectory + "/" + Fernet(key).decrypt(file.encode()).decode())
            except:
                print(Fore.RED + "NAME DECRYPTION ERROR.\n" + Style.RESET_ALL)
                continue

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

def listFilesDecr(fileList, key):
    #translate filenames only
    x = 0;
    for file in fileList:
        print(f'{x}. {Fernet(key).decrypt(file.encode()).decode()}')
        x+=1
    print()

while(True):
    files = refresh()
    inp = input("\n>> ")
    print()
    if inp == "show dir":
        root = tk.Tk()
        root.geometry("10x10")
        filedialog.asksaveasfilename(title="showing current target file", initialdir=currentDirectory)
        root.destroy()
        continue
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
        x = 0;
        for file in files:
            print(f'{x}. {file}')
            x+=1
        print()
        continue
    if inp == "list files decr":
        keyFile = None
        for file in os.listdir(currentDirectory): 
            if file.endswith('.key'): #key found inside directory
                keyFile = file
        if keyFile == None:
            print("no key found here. opening file explorer.\n")
            key = browseFiles()
        else:
            inp = input('confirm password: ')
            print()
            readline = readKey(currentDirectory+'/'+keyFile)
            if inp != readline[1]:
                print('invalid password.\n')
                continue
            key = readline[0]
        listFilesDecr(files, key)
        continue
    if inp.startswith("get key"):
        passw = inp[8::]
        generateKey(passw)
        continue
    if inp == "change dir":
        root = tk.Tk()
        root.geometry("10x10")
        cd = filedialog.askdirectory(title='select directory', initialdir=currentDirectory)
        if cd == '':
            print("no directory selected.\n")
            continue
        currentDirectory = cd
        root.destroy()
        continue
    if inp == "del keys":
        c = 0
        for file in os.listdir(currentDirectory):
            if file.endswith(".key"):
                os.remove(currentDirectory + "/" + file)
                c += 1
        print(f"Deleted {c} keys in this directory.\n")
        continue
    if inp == "del files":
        c = len(files)
        for file in files:
            os.remove(currentDirectory + "/" + file)
        print(f"Deleted {c} files in this directory.\n")
    if inp == "del self":
        os.remove(__file__)
        break
    if inp == "del all":
        for file in os.listdir(currentDirectory):
            if file != os.path.basename(__file__):
                os.remove(currentDirectory + "/" + file)
        os.remove(__file__)
        break
    if inp == "x" or inp == "c" or inp == "e":
        sys.exit()
    print("invalid input.\n")
