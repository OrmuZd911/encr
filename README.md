# encr
### encr.py is a simple tool to encrypt files using the Fernet package in python.
Before running this with Python, make sure you have the tkinter and cryptography packages installed, by running 'pip install tk' and 'pip install cryptography' on the command line.

In order to encrypt files, we need two things: the encr.py file and a key.key file, which can be generated by the encr.py file. Here's how to encrypt your first files using encr.py:

1) Create a directory, and place all the files intended to be encrypted inside.

2) Place the encr.py file inside that directory.

3) To generate a key, run the encr.py file using Python, then enter "get key 1234". Note that 1234 can be replaced by any password you wish.

4) You will notice that a key.key file is generated within that directory. Do not lose this file.

5) While running encr.py, enter "encrypt 1234" and watch as each of your files gets encrypted, along with its name, rendering them unrecognizable! (if the README file is still in this directory, it will be encrypted as well)

6) To decrypt the files, enter "decrypt 1234" and each seemingly unrecognizable file transforms back into its previous form.

Ofcourse, without the key.key file, encrypting or decrypting will not be possible, so you better keep the key.key file somewhere safe if you intend to hide it, as losing the key.key file while having your files encrypted would render them completely unrecoverable. 

The key.key file has the following 2-line format:
[key]
[password]
Any other format would not work, as well as renaming the key.key file.

The password entered for encryption or decryption should match the one within the key.key file, as an added security feature.

## COMMANDS
### list files
Lists all the files that will be processed during encryption/decryption. Does not include sub-directories.
### get key [password]
Generates a key.key file with specified password, necessary for encryption or decryption. If no password is entered, a randomly-generated 6-digit PIN will be created for you.
### encrypt [password]
Encrypts all files within the same directory as the encr.py file. The key must be in the same directory as the files.
### decrypt [password]
Decrypts all files within the same directory as the encr.py file. The key must be in the same directory as the files.
### encrypt select key
Encryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories. In this case, any key name should work, as long as it has the .key extension.
### decrypt select key
Decryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories. In this case, any key name should work, as long as it has the .key extension.
### change dir
Brings up a file explorer to change the target directory.
### x
Closes the window.

# I AM NOT RESPONSIBLE FOR ANY DATA LOSS. FEATURES ARE EXPERIMENTAL. AND DO NOT LOSE THE KEY ON GOD FR
