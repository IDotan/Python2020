def calculate_missing_integridents_cost(actual, order, price):
    '''
    :param actual: dictionary of what is existing in bakery currently
    :param order: dictionary of tommorow's order's list
    :param price: dictionary of ingredients' prices
    :return: total cost for tomorrow's order missing ingredients
    >>> calculate_missing_integridents_cost ({"milk": 5, "eggs": 0, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9}, \
     {"milk": 6, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9},  {"milk": 5, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9})
    149
    >>> calculate_missing_integridents_cost ({"milk": 6, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9}, \
     {"milk": 0, "eggs": 0, "flour": 0, "chocolate": 0, "yeast": 0, "Cornflower": 0},  {"milk": 5, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9})
    0
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 1, "flour": 1, "chocolate": 1, "yeast": 1, "Cornflower": 1},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    20
    >>> calculate_missing_integridents_cost ({"milk": 5, "eggs": 5, "flour":5, "chocolate": 5, "yeast": 5, "Cornflower": 5},\
     {"milk": 10, "eggs": 10, "flour": 10, "chocolate": 10, "yeast": 10, "Cornflower": 10},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    105
    >>> calculate_missing_integridents_cost ({"milk": 5, "eggs": 5, "flour":5, "chocolate": 5, "yeast": 5, "Cornflower": 5},\
     {"milk": 10, "eggs": 10, "flour": 0, "chocolate": 0, "yeast": 0, "Cornflower": 10},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    45
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    180
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 2, "eggs": 1, "flour": 1, "chocolate": 1, "yeast": 1, "Cornflower": 1},  {"milk": 0.5, "eggs": 0.5, "flour":1, "chocolate": 1, "yeast": 1, "Cornflower": 1})
    5.5
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": -1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    Traceback (most recent call last):
        File "<doctest itai7.calculate_missing_integridents_cost[7]>", line 1, in <module>
    ValueError: The price cant be negative
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": 0, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    >>> calculate_missing_integridents_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": 'j', "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    '''
    costs = 0
    while True:
        for i in order.items():
            temp_ingredient = i[0]
            # check if the price dictionary is usable
            if i[0] not in price:
                raise ValueError("There are missing prices")
            if isinstance(price.get(temp_ingredient), str):
                raise ValueError("The price can't be a string")
            if price.get(temp_ingredient) == 0:
                raise ValueError("The price cant be 0")
            if price.get(temp_ingredient) < 0:
                raise ValueError("The price cant be negative")
            # find if there is a need to order more ingredients
            if order[temp_ingredient] > actual[temp_ingredient]:
                amount = order.get(temp_ingredient) - actual.get(temp_ingredient)
                costs += amount * price.get(temp_ingredient)
        return costs


def menu_ingredients():
    """
    A menu option to get the user input for what ingredients are needed
    :return:none, print out if there is no need to order some items nad the total costs of the needed items
    """
    what_we_need = {"milk": 0, "eggs": 0, "flour": 0, "chocolate": 0, "yeast": 0, "Cornflower": 0}
    actual = {"milk": 5, "eggs": 0, "flour": 6, "chocolate": 7, "yeast": 8, "Cornflower": 9}
    price = {"milk": 5, "eggs": 12, "flour": 6, "chocolate": 7, "yeast": 8, "Cornflower": 9}
    printout = ""
    # go over the dict and ask for the user input
    for i in what_we_need.items():
        while True:
            text = "how mach '{}' is needed? if there is no need type in 0\n"
            temp_ingredient = i[0]
            print(text.format(temp_ingredient))
            try:
                temp_input = int(input())
                what_we_need[temp_ingredient] = temp_input
                if temp_input < 0:
                    raise TypeError("cant use negatives")
                # if there are more then what is needed add a massage to the printout
                if what_we_need[temp_ingredient] <= actual[temp_ingredient]:
                    text2 = "There is no need to order {}\n"
                    printout += text2.format(temp_ingredient)
            except TypeError as e:
                print(e)
                continue
            except ValueError:
                print("The input mast be an integer")
                continue
            break
    try:
        costs = calculate_missing_integridents_cost(actual, what_we_need, price)
        # add together all the needed massages to print
        costs_text = ("The total costs are : {}".format(costs))
        printout += costs_text
        print(printout)
    except ValueError as e:
        print(e)


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
    menu_ingredients()