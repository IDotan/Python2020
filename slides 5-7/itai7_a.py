def calculate_missing_ingredients_cost(actual, order, price):
    '''
    :param actual: dictionary of what is existing in bakery currently
    :param order: dictionary of tommorow's order's list
    :param price: dictionary of ingredients' prices
    :return: total cost for tomorrow's order missing ingredients
    >>> calculate_missing_ingredients_cost ({"milk": 5, "eggs": 0, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9}, \
     {"milk": 6, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9},  {"milk": 5, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9})
    149
    >>> calculate_missing_ingredients_cost ({"milk": 6, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9}, \
     {"milk": 0, "eggs": 0, "flour": 0, "chocolate": 0, "yeast": 0, "Cornflower": 0},  {"milk": 5, "eggs": 12, "flour":6, "chocolate":7, "yeast": 8, "Cornflower": 9})
    0
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 1, "flour": 1, "chocolate": 1, "yeast": 1, "Cornflower": 1},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    20
    >>> calculate_missing_ingredients_cost ({"milk": 5, "eggs": 5, "flour":5, "chocolate": 5, "yeast": 5, "Cornflower": 5},\
     {"milk": 10, "eggs": 10, "flour": 10, "chocolate": 10, "yeast": 10, "Cornflower": 10},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    105
    >>> calculate_missing_ingredients_cost ({"milk": 5, "eggs": 5, "flour":5, "chocolate": 5, "yeast": 5, "Cornflower": 5},\
     {"milk": 10, "eggs": 10, "flour": 0, "chocolate": 0, "yeast": 0, "Cornflower": 10},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    45
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": 1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    180
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 2, "eggs": 1, "flour": 1, "chocolate": 1, "yeast": 1, "Cornflower": 1},  {"milk": 0.5, "eggs": 0.5, "flour":1, "chocolate": 1, "yeast": 1, "Cornflower": 1})
    5.5
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": -1, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    Traceback (most recent call last):
        File "<doctest itai7.calculate_missing_integridents_cost[7]>", line 1, in <module>
    ValueError: The price cant be negative
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
     {"milk": 0, "eggs": 0, "flour": 20, "chocolate": 10, "yeast": 10, "Cornflower": 5},  {"milk": 0, "eggs": 2, "flour":3, "chocolate": 4, "yeast": 5, "Cornflower": 6})
    >>> calculate_missing_ingredients_cost ({"milk": 0, "eggs": 0, "flour":0, "chocolate": 0, "yeast": 0, "Cornflower": 0},\
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
        costs = calculate_missing_ingredients_cost(actual, what_we_need, price)
        # add together all the needed massages to print
        costs_text = ("The total costs are : {}".format(costs))
        printout += costs_text
        print(printout)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    menu_ingredients()
