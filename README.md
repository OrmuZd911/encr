# encr
## encr.exe is a simple tool to encrypt files using the Fernet package in Python.

In order to encrypt files, we need two things: the encr.py file and a key.key file, which can be generated by the encr.py file. Here's how to encrypt your first files using encr.py:

1) Create a directory, and place all the files intended to be encrypted inside.

2) Place the encr.py file inside that directory.

3) To generate a key, run the encr.py file using Python, then enter `get key 1234`. Note that 1234 can be replaced by any password you wish.

4) You will notice that a key.key file is generated within that directory. Do not lose this file.

5) While running encr.py, enter `encrypt 1234` and watch as each of your files gets encrypted, along with its name, rendering them unrecognizable! (if the README file is still in this directory, it will be encrypted as well)

6) To decrypt the files, enter `decrypt 1234` and each seemingly unrecognizable file transforms back into its previous form.

Ofcourse, without the key.key file, encrypting or decrypting will not be possible, so you better keep the key.key file somewhere safe if you intend to hide it, as losing the key.key file while having your files encrypted would render them completely unrecoverable. 

The key.key file has the following 2-line format:
[key]
[password]
Any other format would not work, as well as renaming the key.key file.

The password entered for encryption or decryption should match the one within the key.key file, as an added security feature.

# COMMANDS
``` 
list files
```
Lists all the files that will be processed during encryption/decryption. Does not include sub-directories.
```
get key <password>
```
Generates a key.key file with specified password in the target directory, necessary for encryption or decryption. If no password is entered, a randomly-generated 6-digit PIN will be created for you.
```
encrypt <password>
```
Encrypts all files in target directory. The key must also be in the same target directory.
```
decrypt <password>
```
Decrypts all files in target directory. The key must also be in the same target directory.
```
change dir
```
Brings up a file explorer to change the target directory.
```
encrypt select key
```
Encryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories. In this case, any key name should work, as long as it has the .key extension.
```
decrypt select key
```
Decryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories. In this case, any key name should work, as long as it has the .key extension.
``` 
list files decr
```
In a directory full of encrypted files, this lists the true name of all these files by decrypting the file names only. This requires a key, so if a key is not already in the target directory, a file explorer will be opened to manually select the key. This does not encrypt/decrypt any file.
```
del self
```
Deletes itself for quick disposal.
```
del keys
```
**(DANGER)** Deletes all keys in the target directory.
```
del files
```
**(DANGER)** Deletes all target files. Excludes keys and itself.
```
del all
```
**(DANGER)** Deletes everything in target directory, even keys and itself.
```
x/c/e
```
Closes the window.

# I AM NOT RESPONSIBLE FOR ANY DATA LOSS.
### so here are some things to take note of:
#### don't lose keys on god fr
#### please be mindful of your target directory
#### always use 'list files' to double check which files you are about to encrypt
#### large files (above 1GB) have not been tested thorougly. encrypt at your own risk.
