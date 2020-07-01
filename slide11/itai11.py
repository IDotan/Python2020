"""
use to encode or decode a file using "Caesar encrypt"
"""


def encrypt_line(this_line, move_by):
    """
    | encrypt the given line char by char
    :param this_line: the line to be encrypted
    :param move_by: the key of jump to encrypt by
    :return: new encrypted line
    """
    new_line = ""
    # go over each char in the line
    for char in this_line:
        temp_acsii = ord(char)
        # do when the char is a letter
        if 65 <= temp_acsii <= 90 or 97 <= temp_acsii <= 122:
            temp_jump = jump_fix_chr(move_by)
            new_line += encrypt_char(temp_acsii, temp_jump)
        # when there is a space
        elif char == " ":
            new_line += " "
        # to do when the char is a number
        elif 48 <= temp_acsii <= 57:
            temp_jump = jump_fix_num(move_by)
            new_line += encrypt_num(temp_acsii, temp_jump)
        # when its none of the above copy as is
        else:
            new_line += char
    return new_line


def encrypt_num(char_ascii, move_by):
    """
    | encrypt the given char ascii value
    :param char_ascii: the char ascii to be encrypted
    :param move_by: the jump key of the encryption
    :return: the new encrypted char.(chr not ascii)
    """
    # when move_by is 10 its a full loop, return the same chr as the original
    if move_by == 10:
        return chr(char_ascii)
    # add the ascii by the move_by
    temp_ascii = char_ascii + move_by
    # check if the new ascii in a valid range
    if 48 <= temp_ascii <= 57:
        return chr(temp_ascii)
    else:
        # add the min (range - 1) from how mach the ascii got out of range
        temp_encrypted = 47 + (temp_ascii - 57)
        return chr(temp_encrypted)


def encrypt_char(char_ascii, move_by):
    """
    | encrypt the given char ascii value
    :param char_ascii: the char ascii to be encrypted
    :param move_by: the jump key of the encryption
    :return: the new encrypted char.(chr not ascii)
    """
    # 26 mean a full loop, return the same chr as the original
    if move_by == 26:
        return chr(char_ascii)
    # do if it upper case
    if 65 <= char_ascii <= 90:
        return encrypt_char_upper(char_ascii, move_by)
    # do if its lower case
    elif 97 <= char_ascii <= 122:
        return encrypt_char_lower(char_ascii, move_by)


def encrypt_char_upper(char_ascii, move_by):
    """
    | encrypt the given lower ascii value
    :param char_ascii: the lower ascii to be encrypted
    :param move_by: the jump key of the encryption
    :return: the new encrypted char.(chr not ascii)
    """
    # add the ascii by the move_by key
    temp_encrypted = char_ascii + move_by
    # check if the new ascii is in valid range
    if 65 <= temp_encrypted <= 90:
        return chr(temp_encrypted)
    else:
        # add the min (range - 1) from how mach the ascii got out of range
        temp_encrypted = 64 + (temp_encrypted - 90)
        return chr(temp_encrypted)


def encrypt_char_lower(char_ascii, move_by):
    """
    | encrypt the given lower ascii value
    :param char_ascii: the lower ascii to be encrypted
    :param move_by: the jump key of the encryption
    :return: the new encrypted char.(chr not ascii)
    """
    # add the ascii by the move_by key
    temp_encrypted = char_ascii + move_by
    # check if the new ascii is in valid range
    if 97 <= temp_encrypted <= 122:
        return chr(temp_encrypted)
    else:
        # add the min (range - 1) from how mach the ascii got out of range
        temp_encrypted = 96 + (temp_encrypted - 122)
        return chr(temp_encrypted)


def decrypt_line(this_line, move_by):
    """
    | decrypt the given line char by char
    :param this_line: the line to be decrypted
    :param move_by: the key of jump to decrypt by
    :return: new decrypted line
    """
    new_line = ""
    # go over each char in the line
    for char in this_line:
        temp_acsii = ord(char)
        # do when the char is a letter
        if 65 <= temp_acsii <= 90 or 97 <= temp_acsii <= 122:
            temp_jump = jump_fix_chr(move_by)
            new_line += decrypt_char(temp_acsii, temp_jump)
        # when there is a space
        elif char == " ":
            new_line += " "
        # to do when the char is a number
        elif 48 <= temp_acsii <= 57:
            temp_jump = jump_fix_num(move_by)
            new_line += decrypt_num(temp_acsii, temp_jump)
        # when its none of the above copy as is
        else:
            new_line += char
    return new_line


def decrypt_num(char_ascii, move_by):
    """
    | decrypt the given char ascii value
    :param char_ascii: the char ascii to be decrypted
    :param move_by: the jump key of the decryption
    :return: the new decrypted char.(chr not ascii)
    """
    # when move_by is 10 its a full loop, return the same chr as the original
    if move_by == 10:
        return chr(char_ascii)
    # sub the ascii by the move_by key
    temp_ascii = char_ascii - move_by
    # check if the new ascii in a valid range
    if 48 <= temp_ascii <= 57:
        return chr(temp_ascii)
    else:
        # sub the max (range + 1) from how mach the ascii got out of range
        temp_decrypted = 58 - (48 - temp_ascii)
        return chr(temp_decrypted)


def decrypt_char(char_ascii, move_by):
    """
    | decrypt the given char ascii value
    :param char_ascii: the char ascii to be decrypted
    :param move_by: the jump key of the decryption
    :return: the new decrypted char.(chr not ascii)
    """
    # 26 mean a full loop, return the same chr as the original
    if move_by == 26:
        return chr(char_ascii)
    # do if it upper case
    if 65 <= char_ascii <= 90:
        return decrypt_char_upper(char_ascii, move_by)
    # do if its lower case
    elif 97 <= char_ascii <= 122:
        return decrypt_char_lower(char_ascii, move_by)


def decrypt_char_upper(char_ascii, move_by):
    """
    | decrypt the given upper ascii value
    :param char_ascii: the upper ascii to be decrypted
    :param move_by: the jump key of the decryption
    :return: the new decrypted char.(chr not ascii)
    """
    # sub the ascii by the move_by key
    temp_decrypted = char_ascii - move_by
    # check if the new ascii is in valid range
    if 65 <= temp_decrypted <= 90:
        return chr(temp_decrypted)
    else:
        # sub the max (range + 1) from how mach the ascii got out of range
        temp_decrypted = 91 - (65 - temp_decrypted)
        return chr(temp_decrypted)


def decrypt_char_lower(char_ascii, move_by):
    """
    | decrypt the given lower ascii value
    :param char_ascii: the lower ascii to be decrypted
    :param move_by: the jump key of the decryption
    :return: the new decrypted char.(chr not ascii)
    """
    # sub the ascii by the move_by key
    temp_decrypted = char_ascii - move_by
    # check if the new ascii is in valid range
    if 97 <= temp_decrypted <= 122:
        return chr(temp_decrypted)
    else:
        # sub the max (range + 1) from how mach the ascii got out of range
        temp_decrypted = 123 - (97 - temp_decrypted)
        return chr(temp_decrypted)


def jump_fix_chr(move_by):
    """
    | check and edit if needed the number of jumps for letters
    :param move_by: the jump key to check
    :return: the "fixed" jumps to take
    """
    # when more the a full loop, mod the move_by to see how mach really need to move by
    if move_by > 26:
        temp_move_by = move_by % 26
        return temp_move_by
    else:
        return move_by


def jump_fix_num(move_by):
    """
    | check and edit if needed the number of jumps for numbers
    :param move_by: the jump key to check
    :return: the "fixed" jumps to take
    """
    # when more the a full loop, mod the move_by to see how mach really need to move by
    if move_by > 10:
        temp_move_by = move_by % 10
        return temp_move_by
    else:
        return move_by


def encode(file):
    """
    encrypt the given file to ane file with add to the title "_Encode"
    :param file: the file to encrypt
    """
    # open the .txt to encrypt
    with open(file, "r") as this:
        # ask what is the key of jumps to use
        move_by = get_jumps("encryption")
        # open new .txt to write the encryption in
        with open(file[slice(-4)] + "_Encode.txt", 'w') as new:
            # go over each line in the .txt to encrypt
            for line in this:
                # send the line to be encrypted
                encrypted_line = encrypt_line(line, move_by)
                # write the decrypted line to the encrypted file
                new.write(f"{encrypted_line}")


def decode(file):
    """
    decrypt the given file to ane file with add to the title "_Decode"
    :param file: the file to decrypt
    """
    # open the .txt to decrypt
    with open(file, "r") as this:
        # ask what is the key of jumps to use
        move_by = get_jumps("decryption")
        # open a new .txt to write the decryption in
        with open(file[slice(-4)] + "_Decode.txt", 'w') as new:
            # go over each line in the .txt to decrypt
            for line in this:
                # send the line to be decrypted
                decrypted_line = decrypt_line(line, move_by)
                # write the decrypted line to the decrypted file
                new.write(f"{decrypted_line}")


def get_process():
    """
    | ask the user to pick, encrypt or decrypt the file
    :return: 1- encrypt, 2- decrypt, 0- to exit
    """
    while True:
        try:
            task = int(input("Do you want to encrypt or decrypt?\n"
                             "1.Encrypt\n"
                             "2.Decrypt\n"
                             "0.Exit\n"))
            # make sure the input is 1 or 2
            if task not in range(0, 3):
                print("please pick a valid option\n")
                continue
        # when the input is not a number
        except ValueError:
            print("can only input numbers\n")
            continue
        # return when the pick is valid
        return task


def get_jumps(action):
    """
    | get the number of jumps to do to encrypt/decrypt the file
    :param action: string of the action to take
    :return: int number of jumps
    """
    while True:
        try:
            move_by = int(input(f"What is the number of jumps for the {action} process?\n"))
            # check if negative
            if move_by < 0:
                print("cant use a negative\n")
                continue
            # check if 0
            if move_by == 0:
                print("cant use 0\n")
                continue
        except ValueError:
            print("can only input integers\n")
            continue
        # return the num when its valid
        return move_by


def get_file():
    """
    | get the file name/and path from the user
    :return: the file name/and path
    """
    file = input("What file do you want to use?\n")
    # make sure there is no space in the input
    if " " in file:
        print("Cant have a space in the file path/name, please reenter\n")
        # recall get_file
        get_file()
    # make sure not empty
    if "" == file:
        print("Cant stay empty\n")
        # recall get_file
        get_file()
    return file


def menu():
    """
    | a menu to be shown to the user and get his input
    """
    while True:
        # ask what the user want to do
        task = get_process()
        # when task is 0, close the script
        if task == 0:
            exit()
        # loop for the file and the task it self
        while True:
            try:
                # get the file to process
                file = get_file()
                # do an encryption
                if task == 1:
                    encode(file)
                    break
                # do a decryption
                else:
                    decode(file)
                    break
            except FileNotFoundError:
                print("The file was unreachable, please try again\n")
                continue
        # print when all went well
        print("The process was complete\n")


if __name__ == "__main__":
    menu()
