

def rate_password(username, passwd):
    '''
    :param username: the user's username
    :param passwd: password to test
    :return: rate for this password
    >>> rate_password('vd', '123456')
    3
    >>> rate_password('vd','123456abc')
    6
    >>> rate_password('vd', '123456Abc')
    8
    >>> rate_password('vd', '123456Abc$')
    10
    >>> rate_password('vd', '12j45')
    4
    >>> rate_password('vd', '123456')
    3
    >>> rate_password('vd', 'aaaaaa')
    3
    >>> rate_password('vd', 'AAAAAA')
    3
    >>> rate_password('vd', '*?*}**')
    4
    >>> rate_password('vd', 'Aa1*23')
    9
    >>> rate_password('vd', 'aAaaaa')
    5
    >>> rate_password('vd', 'Aa1*234')
    9
    >>> rate_password('vd', 'Aa1*23456')
    10
    '''
    id = str(username)
    psw_to_test = str(passwd)
    length = len(psw_to_test)
    psw_score = 0
    cap = 0
    low = 0
    num = 0
    sym = 0
    # make sure the password is longer then 4
    if length <= 4:
        raise ValueError("password must include minimum of 5 characters")
    # make sure the username is not used in the password
    if id in psw_to_test:
        raise ValueError("can't have the username in the password")
    # go over the password to check what characters are included
    i = 0
    j = 1
    while i < length:
        temp_char = (psw_to_test[slice(i, j)])
        temp_acsii = ord(str(temp_char))
        if temp_acsii == 32:
            raise ValueError("can't have spaces in the password")
        # check if the chr is a capital letter
        if 65 <= temp_acsii <= 90:
            # raise the count only if it wasn't increased before
            if cap == 0:
                cap = 1
                psw_score += 1
        # check if the chr is a lower letter
        elif 97 <= temp_acsii <= 122:
            # raise the count only if it wasn't increased before
            if low == 0:
                low = 1
                psw_score += 1
        # check if the chr is a number
        elif 48 <= temp_acsii <= 57:
            # raise the count only if it wasn't increased before
            if num == 0:
                num = 1
                psw_score += 1
        # check if the chr is a symbol
        elif 33 <= temp_acsii <= 46 or 58 <= temp_acsii <= 64 \
                or 91 <= temp_acsii <= 96 or 123 <= temp_acsii <= 126:
            # raise the count only if it wasn't increased before
            if sym == 0:
                sym = 1
                psw_score += 2
        else:
            raise ValueError("one or more of the characters in the password are invalid")
        i += 1
        j += 1
    # sum up the ranking of the password
    # rank the password length
    if length < 6:
        psw_score += 1
    elif 6 <= length <= 8:
        psw_score += 2
    else:
        psw_score += 3
    # rank by how many different char types are used
    chr_sum = cap + low + num + sym
    if chr_sum == 2:
        psw_score += 1
    if chr_sum > 2:
        psw_score += 2
    return psw_score


# not in use but left in if there will need to be changes
def no_space(*args):
    """
    make sure the password have no space in it
    :param args: the password to check
    :return:
    """
    temp = list(args)
    temp1 = str(temp[0])
    temp_psw = []
    i = 0
    j = 1
    length = len(temp1)
    while i < length:
        temp_char = (temp1[slice(i, j)])
        temp_psw.append(temp_char)
        temp_acsii = ord(str(temp_char))
        if temp_acsii == 32:
            raise ValueError("space")
        i += 1
        j += 1


# not in use but left in if there will need to be changes
def length_test(psw):
    """
    make sure the password length is in the approved range
    :param psw: the password the check its length
    :return:
    """
    length = len(psw)
    if length <= 4:
        raise ValueError("password must be include minimum of 4 characters")


def ranking(score):
    """
    assign string to the number ranking, from week to very strong
    :param score: password's rank
    :return: a string representing the password rank
    >>> ranking(3)
    your password rank is:
     week
    >>> ranking(4)
    your password rank is:
     week
    >>> ranking(5)
    your password rank is:
     fair
    >>> ranking(6)
    your password rank is:
     fair
    >>> ranking(7)
    your password rank is:
     strong
    >>> ranking(8)
    your password rank is:
     very strong
    >>> ranking(9)
    your password rank is:
     very strong
    >>> ranking(20)
    your password rank is:
     very strong

    """

    # assign a string ranking to the found password score
    if score <= 4:
        rank = "week"
    if 5 <= score <= 6:
        rank = "fair"
    if score == 7:
        rank = "strong"
    if score > 7:
        rank = "very strong"
    return print("your password rank is:\n", rank)


def menu_password():
    """
    A menu to get the user username and password
    :return: none, printout how strong the given password is
    """
    while True:
        print("please enter ID:\n")
        try:
            id = input()
            empty = ""
            # make sure the user name is not empty
            if len(id) == 0 and empty in id:
                raise TypeError("The username cant be empty")
            if chr(32) in id:
                raise TypeError("Can't have spaces in the username")
        except TypeError as e:
            print(e)
            continue
        break
    while True:
        print("please enter password:\n")
        psw = input()
        try:
            rank = rate_password(id, psw)
        except ValueError as e:
            print(e)
            continue
        break
    ranking(rank)


if __name__ == "__main__":
    menu_password()
