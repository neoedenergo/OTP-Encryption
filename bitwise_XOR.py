import numpy as np
import os
import sys
import hashlib

######### keygen + checksum generation #############
def keygen():
    key_list = []
    for x in range(int(sys.argv[2])):
        key_list.append(ord(os.urandom(1)))
    f = open(sys.argv[3] + ".key", 'wb')
    f.write(bytes(key_list))
    f.close()
    print("\n Keyfile created.\n")

    f_to_checksum = open(sys.argv[3] + ".key", "rb").read()
    checksum = hashlib.sha512(f_to_checksum).hexdigest()
    f2 = open((sys.argv[3] + ".key" + ".sha512"), "x")
    f2.write(checksum)
    f2.close()
    print("\n The sha512 checksum file has been created.\n")
##############################


######### encrypt ############
def encrypt():
    file = open(sys.argv[2], "rb")
    byte_list = file.read()
    byte_list2 = []
    for x in byte_list:
        byte_list2.append(x)

    file2 = open(sys.argv[3], "rb")
    key_list = file2.read()
    key_list2 = []
    for x in key_list:
        key_list2.append(x)
    
    key_list2 = key_list2[:len(byte_list2)]

    result_list = np.bitwise_xor(byte_list2, key_list2).tolist()
    
    f = open(sys.argv[2] + ".enc", 'wb')
    f.write(bytes(result_list))
    f.close()

    print("\n The encrypted file has been created.\n")

    f_to_checksum = open(sys.argv[2] + ".enc", "rb").read()

    checksum =  hashlib.sha512(f_to_checksum).hexdigest()
    f2 = open((sys.argv[2] + ".enc" + ".sha512"), "x")
    f2.write(checksum)
    f2.close()
    print("\n The sha512 checksum file has been created.\n")
##############################


########## decrypt ###########
def decrypt():
    file = open(sys.argv[2], "rb")
    byte_list = file.read()
    byte_list2 = []
    for x in byte_list:
        byte_list2.append(x)

    file2 = open(sys.argv[3], "rb")
    key_list = file2.read()
    key_list2 = []
    for x in key_list:
        key_list2.append(x)
    
    key_list2 = key_list2[:len(byte_list2)]

    result_list = np.bitwise_xor(byte_list2, key_list2).tolist()
    
    f = open(sys.argv[2].replace(".enc", ".dec"), 'wb')
    f.write(bytes(result_list))
    f.close()
##############################


######### checksum ###########
def checksum():
    file = open((sys.argv[2]), "rb").read()
    checksum_file = open((sys.argv[3]), "r").read()
    checksum = hashlib.sha512(file).hexdigest()
    print("\n " + checksum_file + "\n " + checksum + "\n")
    if checksum == checksum_file :
        print("\n - SUCCESS -   The checksum matches\n")
    else:
        print("\n - FAILED -   The checksum does NOT match\n")
##############################


######### main ###############
if sys.argv[1] == "keygen":
    keygen()
elif sys.argv[1] == "encrypt":
    encrypt()
elif sys.argv[1] == "decrypt":
    decrypt()
elif sys.argv[1] == "checksum":
    checksum()
elif sys.argv[1] == "help":
    print("\nThis program generates keys for the bitwise XOR cipher, also encrypts and decrypts files using the keys and generates and checks checksums.\nUse 'python3 bitwise_XOR.py keygen lenght_of_key filename_or_path_to_save_key_to' for key generation.\nUse 'python3 bitwise_XOR.py encrypt file_to_encrypt keyfile_to_use' to encrypt.\nUse 'python3 bitwise_XOR.py decrypt file_to_decrypt keyfile_to_use' to decrypt.\nUse 'python3 bitwise_XOR.py checksum file checksum_file' to perform the check.\nUse 'python3 bitwise_XOR.py help' to show this help message.\n")
else:
    print("\nWrong arguments, enter 'python3 bitwise_XOR.py help' for guidance on how to use this program.\n")
##############################