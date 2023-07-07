# encr: a simple tool to encrypt files.
Note that the Python file in the repository is only to show the Python code within. Unless you are interested, it can be deleted.

## How to use?
In order to encrypt files, we only need encr.exe and a .key file generated with encr.exe.
Here's how you can encrypt your first files:

1) Create a directory, and place all the files intended to be encrypted inside.

2) Place the `encr.exe` file inside that directory.

3) To generate a key, run `encr.exe`, then enter `get key 1234`. Note that `1234` can be replaced by any password you wish. This creates a key for encryption, along with a required password to activate it.

4) You will notice that a `key.key` file is generated within that directory. DO NOT lose this file or forget the password to this file.

5) Enter `encr 1234` and watch as each of your files gets encrypted, along with its name, rendering them unrecognizable! (if the README file is still in this directory, it will be encrypted as well)

6) To decrypt the files, enter `decr 1234` and each seemingly unrecognizable file transforms back into its previous form.

Ofcourse, without the key.key file, encrypting or decrypting will not be possible, so you better keep the key.key file somewhere safe if you intend to hide it, as losing the key.key file while having your files encrypted would render them completely unrecoverable. The password entered for encryption or decryption should match the one created with the key.key file, as an added security feature. Note that this program can only encrypt/decrypt folders of files, not individual files.

## Commands
`list`: 
Lists all the files that will be processed during encryption/decryption. Does not include sub-directories.

`get key <password>`:
Generates a key.key file with specified password in the target directory, necessary for encryption or decryption. If no password is entered, a randomly-generated 6-digit PIN will be created for you. DO NOT lose this file or forget the password to this file.

`encr <password>`:
Encrypts all files in target directory. The key must also be in the same target directory.

`decr <password>`:
Decrypts all files in target directory. The key must also be in the same target directory.

`change`:
Brings up a file explorer to change the target directory.

`show`:
Shows the target directory in a file explorer. Close the explorer to return.

`encr select key`:
Encryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories.

`decr select key`:
Decryption using key that is located outside the target directory, this brings up file explorer for you to find the key in other directories.

`single`:
In a directory full of encrypted files, this allows to decrypt only a single file, then automatically opens it to be used. After usage, the file is automaticalled re-encrypted. This requires a key, so if a key is not already in the target directory, a file explorer will be opened to manually select the key. This is especially useful if you have huge folder full of encrypted files and you only want to access one without waiting for the entire folder to be decrypted.

`del self`:
Deletes itself for quick disposal.

`del keys`:
**(DANGER)** Deletes all keys in the target directory.

`del files`:
**(DANGER)** Deletes all target files. Excludes keys and itself.

`del all`:
**(DANGER)** Deletes everything in target directory, even keys and itself.

`x/c/e`:
Closes the window.

# I AM NOT RESPONSIBLE FOR ANY DATA LOSS.
### so here are some things to take note of:
#### don't lose keys on god fr
#### always pay attention to target directory
#### always use `list` to double check which files you are about to encrypt
#### large files (above 1GB) have not been tested thorougly. encrypt at your own risk.
