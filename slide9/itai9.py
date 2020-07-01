import time

"""
module to mange and control a parking lot
"""


class Car:
    """
    | class car to mange cars in the parking lot
    """

    def __init__(self, enter_time=time.localtime(), plate="1234", v_type="private", tel=1234):
        """
        | create a new car.
        :param enter_time: the time the car got in the parking lot
        :param plate: the car plate num
        :param v_type: what is the vehicle type. privet or public
        :param tel: the telephone number of the driver
        """
        self.__time = enter_time
        self.__plate = plate
        self.__v_type = v_type
        self.__tel = tel

    def set_plate(self, new_plate):
        """
        | set the plate of the giving car
        :param new_plate: the plate num to be change to
        """
        # make sure the plate is not empty
        if new_plate == "":
            raise ValueError("can't have an empty plate number")
        self.__plate = new_plate

    def set_tel(self, new_tel):
        """
        | set the  telephone of the given car
        :param new_tel: the telephone to be change to
        """
        # make sure the phone is not empty
        if new_tel == "":
            raise ValueError("can't have empty phone number")
        self.__tel = new_tel

    def set_v_type(self, new_type):
        """
        | set the vehicle type of the given car.
        :param new_type: the type to be change to, private or public
        """
        # make sure the type is a valid one
        if not (new_type.lower() == "private" or new_type.lower() == "public"):
            raise TypeError("not a valid vehicle type")
        else:
            self.__v_type = new_type.lower()

    def get_plate(self):
        """
        | get the plate number of the vehicle
        :return: vehicle's plate number
        """
        return self.__plate

    def get_v_type(self):
        """
        | get the vehicle type
        :return: vehicle type
        """
        return self.__v_type

    def get_tel(self):
        """
        | get the telephone number
        :return: telephone number
        """
        return self.__tel

    def get_time(self):
        """
        | get the enter time of the vehicle in seconds since the epoch
        :return: the time the vehicle got in the parking lot
        """
        return self.__time

    def car_info(self):
        """
        | string of all the info of the car
        :return: string of the car info
        """
        # get all the variables to be sent
        __p = self.get_plate()
        __v = self.get_v_type()
        __tel = self.get_tel()
        # get and format the time
        __time = time.strftime("%m/%d/%Y, %H:%M:%S", self.__time)
        return f"plate: {__p} type: {__v}\n" \
               f"telephone: {__tel}\n" \
               f"entry time: {__time}"


class ParkingLot:
    """
    | class parking lot to mange
    """

    def __init__(self, max_space=10, price=15):
        """
        | create new parking lot
        :param max_space: the max space for cars. default 10.
        :param price: price per hours of parking. default 15.
        """
        self.__cars = []
        self.__max_space = max_space
        self.__price = price

    def __add__(self, new_car):
        """
        | adds new car in to the parking lot
        :param new_car: the car class item to add
        """

        # go over the cars in the lot one by one
        for i in self.__cars:
            # make sure there is no car in the lot with the same plate number
            if i.get_plate() == new_car.get_plate():
                raise ValueError(f"There is a car with the plate number '{new_car.get_plate()}' in the lot")
        # make sure there is space for a new car
        if len(self.__cars) < self.__max_space:
            # add the car to the lot
            self.__cars.append(new_car)
        else:
            raise IndexError("no more room in the parking lot")

    def __sub__(self, exit_car):
        """
        | remove a car for the parking lot
        :param exit_car: the car to be removed from the lot
        """
        # make sure the parking lot is not empty
        if len(self.__cars) == 0:
            raise IndexError("cant remove a car when the lot is empty")
        # go over the cars in the lot one by one
        for i in self.__cars:
            # make sure there is no car in the plot with the same plat number
            if i.get_plate() == exit_car.get_plate():
                # remove the car from the lot
                self.__cars.remove(i)
                return
        raise IndexError(f"There is no car with {exit_car.get_plate()} plate number in the lot")

    def general_report(self):
        """
        | print out general report of the cars in the lot ,all cars plate and there type
        """
        # make sure the parking lot is not empty before doing a deeper scan
        if len(self.__cars) == 0:
            print("The parking lot is empty right now\n")
            return
        # variables to use
        __space = 0
        __private = 0
        __public = 0
        __report_end = ""
        # go over the cars in the lot one by obe
        for i in self.__cars:
            if i.get_v_type() == "private":
                __private += 1
            else:
                __public += 1
            __space += 1
            # add the car i to the string of the report
            __report_end += f"{__space}.{i.get_v_type()}, plate number: {i.get_plate()}\n"
        # create an opening line for the report
        __report = f"Total of {__space} car\\s, {__private} private vehicle\\s and {__public} public vehicle\\s :\n"
        print(__report, __report_end, sep='')

    def set_price(self, new_price):
        """
        | set the price of the parking
        :param new_price: the new price to set
        """
        # make sure the new price is a valid number
        if isinstance(new_price, int) or isinstance(new_price, float):
            if new_price == 0:
                raise ValueError("the price cant be 0")
            if new_price < 0:
                raise ValueError("the price cant be a negative")
            # when all checks have passed set the new price
            self.__price = new_price
        else:
            raise ValueError("the price can only be a number")

    def get_price(self):
        """
        | get the price per hour
        :return: int of the price
        """
        return self.__price

    def set_max_space(self, new_space):
        """
        | set new max space for the parking lot
        :param new_space: the new max space
        """
        # make sure the new space have a valid value
        if isinstance(new_space, int):
            if new_space == 0:
                raise ValueError("the space cant be 0")
            if new_space < 0:
                raise ValueError("the space cant be a negative")
            # make sure the new space is not less then the num of cars in the lot
            if new_space < len(self.__cars):
                raise ValueError(
                    f"the space cant be less then the number of cars in the lot witch is {len(self.__cars)}")
            # when all check have passed set the new space
            self.__max_space = new_space
        else:
            raise ValueError("the space can only be an integer")

    def more_then_24h(self):
        """
        | print the plate and phone number of cars who are parked for 24H or more
        """
        # go over the cars in the lot one by one
        __report = ""
        num = 1
        for i in self.__cars:
            __temp_time = i.get_time()
            # check if 24h have passed, 24H = 86400 sec
            if time_passed(__temp_time) >= 86400:
                __report += f"{num}. plate: {i.get_plate()} phone: {i.get_tel()}"
            num += 1
        # check if any cars where found
        if not __report == "":
            print(__report)
        else:
            # default print when no cars are parked for over 24H
            print("no car have been parked for more then 24H\n")

    def how_many_parked(self):
        """
        | get the number of cars parked in the parking lot
        :return: int, how many cars are parked
        """
        return len(self.__cars)

    def get_cars(self):
        """
        | get the list of cars in the lot
        :return: the car in the given index
        """
        return self.__cars

    def get_max_space(self):
        """
        | give the max space in the parking lot
        :return: the max space in the parking lot
        """
        return self.__max_space


class Users:
    """
    | class to mange users of the parking lot
    """

    def __init__(self):
        """
        | create empty user list
        """
        self.__user_list = []

    def add_user(self, user, psw):
        """
        | add new user to the users dic
        :param user: the id of the user
        :param psw: the password of the user
        """
        self.__user_list.append({user: psw})

    def remove_user(self, user):
        """
        | remove user for the dic
        :param user: the user to be removed
        """
        # make sure the user list is not empty
        if len(self.__user_list) == 0:
            raise IndexError("the user list is empty")
        index = 0
        # go over the list one by one
        for i in self.__user_list:
            if user in i:
                # when the user is found remove it
                self.__user_list.pop(index)
                return
            index += 1
        # when reaching the end with out a match raise error
        raise ValueError(f"ID: '{user}' is not in the system")

    def valid_user(self, user, psw):
        """
        | check if the given user and psw are in the system and are a mach
        :param user: the user id
        :param psw: the password of the user
        :return: True if in the system and matching password
        """
        # make sure the user list is not empty
        if len(self.__user_list) == 0:
            raise IndexError("the user list is empty")
        # go over the list one by one
        for i in self.__user_list:
            if user in i:
                # when the user is found check if the password is a match
                if psw == i.get(user):
                    return True
                else:
                    raise ValueError("the user name and password don't match\n")
        # when reaching the end with out a match raise error
        raise ValueError(f"ID: '{user}' is not in the system")

    def user_list(self):
        """
        | return a list of users ID
        :return: return a list of users ID
        """
        list = []
        for i in self.__user_list:
            for user in i:
                list.append(user)
        return list

    def reset_to_default(self):
        """
        | Reset the user list to its default
        """
        self.__user_list = [{'admin': 'admin'}]


def time_passed(test_time):
    """
    | calculate time passed from entry
    :param test_time: the time to be checked against current time
    :return: the sec witch have passed from time of entry
    """
    # subtract the current time for the given time (in seconds)
    return (time.mktime(time.localtime())) - (time.mktime(test_time))


def log_in():
    """
    | check if the user is in the system and then check if the password match
    :return: True if the user is in the system
    """
    user = input("Enter ID:\t")
    # make sure there isn't the same ID already in the system
    if user not in u.user_list():
        print(f"The user {user} is not in the system\n")
        return
    psw = input("Enter password:\t")
    # send ID and password to be verified
    return u.valid_user(user, psw)


def add_car_plate(temp_car):
    """
    | get input of the car plate from the user and set it to the temp car
    """
    while True:
        try:
            plate = input("plate number:\t")
            temp_car.set_plate(plate)
            break
        except ValueError as e:
            print(e)
            continue


def add_car_phone(temp_car):
    """
    | get input of the car driver phone number and set it to the temp car
    """
    while True:
        try:
            phone = input("telephone number:\t")
            temp_car.set_tel(phone)
            break
        except ValueError as e:
            print(e)
            continue


def add_car_type(temp_car):
    """
    | get the vehicle type from the user and set it to the temp car
    """
    while True:
        try:
            type_pick = int(input("pick: 1.private 2.public\n"))
        except ValueError:
            print("can only input numbers")
            print("")
            continue
        if type_pick not in range(1, 3):
            print("please pick a valid option\n")
            continue
        # set the type base on the input
        if type_pick == 1:
            temp_car.set_v_type("private")
        else:
            temp_car.set_v_type("public")
        break


def add_car(lot):
    """
    | ask for input of the car to add to the lot
    :param lot: the parking lot to ad the car to
    """
    # make sure there is room in the parking lot
    if lot.how_many_parked() == lot.get_max_space():
        print("the parking lot is full\n")
        return
    # create a new car object with the info from the user and the current time
    temp_car = Car()
    # ask the user for the car info to be added
    add_car_plate(temp_car)
    add_car_phone(temp_car)
    add_car_type(temp_car)
    try:
        # add the new car to the lot
        lot + temp_car
    except ValueError as e:
        print(f"{e}\n")
    except IndexError as e:
        print(f"{e}\n")


def remove_car(lot):
    """
    | remove a car form the parking lot and print how mach is needed to pay
    :param lot: the parking lot
    """
    # check if the parking lot is not empty
    if lot.how_many_parked() == 0:
        print("the parking lot is empty\n")
        return
    plate = input("Enter plate number of the car to remove:\t")
    # go over the car list to find the car we want to remove for the lot
    for i in lot.get_cars():
        if i.get_plate() == plate:
            """
            # divide the time parked by seconds in an hour round down then multiply it by the price
            sum_to_pay = (int(time_passed(i.get_time()) / 3600)) * lot.get_price()
            """
            # get the days and hours that have passed since the car parked
            hour, day = time_to_pay_for(time_passed(i.get_time()))
            # multiply day by 24 to convert to hours add the hours then multiply buy the cost
            sum_to_pay = ((day * 24) + hour) * lot.get_price()
            print(f'need to pay {sum_to_pay}₪\n')
            # remove the car with the matching plat number
            lot - i
            return
    raise ValueError("no car with a matching plate number was found")


def time_to_pay_for(car_time):
    """
    | get the hour and days that have passed and need to charge for
    :param car_time: the car entry time
    :return: hour, day - chargeable hours,  chargeable days
    """
    # make sure the time is valid (not negative)
    if car_time > 0:
        # convert the time in sec to time struct
        temp_time = time.gmtime(car_time)
        # get the variables needed from the time object
        hour = temp_time.tm_hour
        # remove 1 day as the count start from 1 and not 0
        day = temp_time.tm_yday - 1
        return hour, day
    else:
        return 0, 0


def set_price(lot):
    """
    | set price of the given parking lot
    :param lot: the parking lot to change it's price
    """
    while True:
        try:
            # ask the user for the price and check if its valid
            try:
                price = float(input("Enter the new price:\t"))
            except ValueError:
                print("must be a number\n")
                continue
            # when the price is valid change the price in the lot
            lot.set_price(price)
            break
        except ValueError as e:
            print(e)
            continue


def set_space(lot):
    """
    | set new max parking spaces on the given lot
    :param lot: the parking lot to change its max space
    """
    while True:
        try:
            # first and basic input test to make sure its an integer
            space = int(input("Enter the new max space you want to set:\t"))
        except ValueError:
            print("can only be a integer\n")
            continue
        try:
            # send the new max space to be set
            lot.set_max_space(space)
            break
        except ValueError as e:
            print(f"{e}\n")
            continue


def see_registered():
    """
    | print the registered users ID in a list
    """
    temp_list = u.user_list()
    # check if there is no ID in the list
    if len(temp_list) == 0:
        print("There are no registered users in the system\n")
        return
    num = 1
    print_this = ""
    # go over the list and add the ID to a str
    for i in temp_list:
        print_this += f"{num}.{i}\n"
        num += 1
    print(print_this)


def valid_id_psw(str):
    """
    | validate the legality of the giving ID or password and give score indicators to the password
    :param str: the string to be validated
    :return: (cap, low, num, sym) the score the str got, if not valid raise
    """
    # initialize the score variables
    cap, low, num, sym = 0, 0, 0, 0
    # go over the str rank and validate the ch is legal
    for ch in str:
        temp_acsii = ord(ch)
        # check if the ch is a capital letter
        if 65 <= temp_acsii <= 90:
            cap = 1
        # check if the ch is a lower letter
        elif 97 <= temp_acsii <= 122:
            low = 1
        # check if the ch is a number
        elif 48 <= temp_acsii <= 57:
            num = 1
        # check if the ch is a symbol
        elif 33 <= temp_acsii <= 46 or 58 <= temp_acsii <= 64 \
                or 91 <= temp_acsii <= 96 or 123 <= temp_acsii <= 126:
            sym = 1
        else:
            raise ValueError("one or more of the characters are invalid")
    return cap, low, num, sym


def get_user_id():
    """
    | get the user ID and password after validating them
    :return: true/false, user - to go back to menu, the user ID
    """

    while True:
        user = input("\nCan include only English letters, numbers and symbols\n"
                     "Enter 0 to go back to the menu\n"
                     "Enter ID:\t")
        # go back to the menu if 0 is entered
        if user == '0':
            return True, ""
        # short password checks
        if len(user) == 0 and "" in user:
            print("ID cant be empty")
            continue
        if " " in user:
            print("ID cant have spaces")
            continue
        if user in u.user_list():
            print("This user name is taken")
            continue
        try:
            # make sure the ID is valid
            valid_id_psw(user)
            return False, user
        except ValueError as e:
            print(e)
            continue


def get_password(user):
    """
    | get the password from the user and validate it
    :param user: the valid user ID
    :return: true/false, password - true to go back to menu, the new user password
    """
    while True:
        psw = input("\nMust include at lest one of: capital and lowe letters, numbers, symbols\n"
                    "Enter 0 to go back to the menu\n"
                    "Enter password:\t")
        # go back to the menu if 0 is entered
        if psw == '0':
            return True, ""
        # short password checks
        if len(psw) <= 4:
            print("password must include minimum of 5 characters")
            continue
        if user in psw:
            print("can't have the username in the password")
            continue
        if " " in psw:
            print("cant have spaces in the password\n")
            continue
        try:
            # send the password to be validated and get score indicators
            cap, low, num, sym = valid_id_psw(psw)
            # get str rank from the score
            rank = rank_password(len(psw), cap, low, num, sym)
            user_psw = keep_password(psw, rank)
            # when user_psw is not "" the password was confirmed
            if user_psw != "":
                return False, user_psw
            # when user_psw is "" the user want to pick a different password
            else:
                continue
        except ValueError as e:
            print(e)
            continue


def keep_password(psw, rank):
    """
    | showing password rank and asking the user to confirm the password
    :param psw: the password
    :param rank: str rank of the password
    :return: "" - to pick a new password, otherwise return the password
    """
    while True:
        task = int(input(f"\nyour password rank is: {rank}.\n"
                         f"1.To keep it\n"
                         f"2.To enter new one\n"))
        # do the task wanted base of the given input
        if task == 1:
            # return the confirmed password
            return psw
        elif task == 2:
            # return "" to symbolize wanting to pick a new password
            return ""
        else:
            print("please pick a valid option")
            continue


def rank_password(length, cap, low, num, sym):
    """
    give a number score to the password
    :param length: password length
    :param cap: 1 if there capital letter in the password
    :param low: 1 if there lower letter in the password
    :param num: 1 if there numbers in the password
    :param sym: 1 if there symbols in the password
    :return: str of the password rank
    """
    psw_score = 0
    # length rank
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
    elif chr_sum > 2:
        psw_score += 2
    # add score for using each character type
    psw_score += cap + low + num
    # if there are symbols in the password get 2 points to the rank
    if sym == 1:
        psw_score += 2
    # send number score to str_tanking() to get the str of the rank
    return str_ranking(psw_score)


def str_ranking(score):
    """
    | give a sting rank to the password to be used
    :param score: the number score of the password
    :return: str of the rank
    """
    if score <= 4:
        rank = "week"
    elif 5 <= score <= 6:
        rank = "fair"
    elif score == 7:
        rank = "strong"
    elif score > 7:
        rank = "very strong"
    return rank


def add_new_user():
    """
    | add new user to the authorized list
    """
    # ask for the user ID
    back_to_menu, user_id = get_user_id()
    if back_to_menu:
        return
    # ask for the user psw
    back_to_menu, psw = get_password(user_id)
    if back_to_menu:
        return
    # add the new user to the authorized user list
    u.add_user(user_id, psw)


def remove_user():
    """
    | remove user from the authorized list
    """
    try:
        user = input("Enter the ID of the user you want to remove:\n")
        # check if the given user is listed
        if user not in u.user_list():
            print(f"The user '{user}' is not in the system\n")
            return
        psw = input("Please enter the ID's password:\n")
        # make sure the user and password are a mach before removing
        if u.valid_user(user, psw):
            u.remove_user(user)
        else:
            print("The user ID and password did not match\n")
            return
    except ValueError as e:
        print(e)


def users_menu():
    """
    | menu for manging the parking lot users
    """
    while True:
        try:
            task = int(input("1.See registered users list\n"
                             "2.Add new user\n"
                             "3.Remove user\n"
                             "4.Reset authorized users to default\n"
                             "0.Go back\n"))
        except ValueError:
            print("can only input numbers\n")
            continue
        # make sure the num is a valid option
        if task not in range(0, 5):
            print("please pick a valid option\n")
            continue
        # go over to option and do what was asked
        if task == 0:
            if len(u.user_list()) == 0:
                print("user list cant stay empty when leaving this menu")
                continue
            break
        elif task == 1:
            see_registered()
        elif task == 2:
            add_new_user()
        elif task == 3:
            remove_user()
        elif task == 4:
            u.reset_to_default()


def not_logged_menu(lot):
    """
    | menu options when the user is not logged in
    :param lot: the lot we are manging
    :return: (tre/false, lot) - (login status, the lot witch is manged)
    """
    while True:
        try:
            task = int(input("1.Log-in\n"
                             "2.Add car to the parking lot\n"
                             "3.Remove car from the parking lot\n"
                             "4.Report of cars parked for more then 24H\n"
                             "5.General report of cars in the parking lot\n"
                             "0.Exit\n"))
        except ValueError:
            print("can only input numbers\n")
            continue
        # make sure the num is a valid option
        if task not in range(0, 6):
            print("please pick a valid option\n")
            continue
        # go over the different option and do what was asked
        if task == 0:
            exit()
        elif task == 1:
            try:
                if log_in():
                    return True, lot
            except ValueError as e:
                print(e)
        elif task == 2:
            try:
                add_car(lot)
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 3:
            try:
                remove_car(lot)
            except ValueError as e:
                print(f"{e}\n")
                continue
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 4:
            try:
                lot.more_then_24h()
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 5:
            try:
                lot.general_report()
            except AttributeError:
                print("there is no parking lot initialized\n")


def logged_in_menu(lot):
    """
    | menu options when the user is logged in
    :param lot: the lot we are manging
    :return: (true/false, lot) - (login status, the lot witch is manged)
    """
    while True:
        try:
            task = int(input("1.Create new parking lot\n"
                             "2.Add car to the parking lot\n"
                             "3.Remove car from the parking lot\n"
                             "4.Report of cars parked for more then 24H\n"
                             "5.General report of cars in the parking lot\n"
                             "6.Change parking price\n"
                             "7.Change max parking spots\n"
                             "8.Uses management menu\n"
                             "9.Log out\n"
                             "0.Exit\n"))
        except ValueError:
            print("can only input numbers\n")
            print("")
            continue
        # make sure the num is a valid option
        if task not in range(0, 10):
            print("please pick a valid option\n")
            continue
        # go over the different option and do what was asked
        if task == 0:
            exit()
        elif task == 9:
            return False, lot
        elif task == 1:
            lot = ParkingLot()
            continue
        elif task == 2:
            try:
                add_car(lot)
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 3:
            try:
                remove_car(lot)
            except ValueError as e:
                print(f"{e}\n")
                continue
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 4:
            try:
                lot.more_then_24h()
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 5:
            try:
                lot.general_report()
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 6:
            try:
                set_price(lot)
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 7:
            try:
                set_space(lot)
            except AttributeError:
                print("there is no parking lot initialized\n")
        elif task == 8:
            users_menu()


def task_test(task):
    no_parking_lot_msg = "there is no parking lot initialized\n"
    # go over the different option and do what was asked
    global logged
    global lot_test
    if task == 0:
        exit()
    elif task == 9:
        logged = False
    elif task == 1:
        if logged:
            lot_test = ParkingLot()
        else:
            try:
                if log_in():
                    logged = True
            except ValueError as e:
                print(e)
    elif task == 2:
        try:
            add_car(lot_test)
        except AttributeError:
            print(no_parking_lot_msg)
    elif task == 3:
        try:
            remove_car(lot_test)
        except ValueError as e:
            print(f"{e}\n")
        except AttributeError:
            print(no_parking_lot_msg)
    elif task == 4:
        try:
            lot_test.more_then_24h()
        except AttributeError:
            print(no_parking_lot_msg)
    elif task == 5:
        try:
            lot_test.general_report()
        except AttributeError:
            print(no_parking_lot_msg)
    elif task == 6:
        try:
            set_price(lot_test)
        except AttributeError:
            print(no_parking_lot_msg)
    elif task == 7:
        try:
            set_space(lot_test)
        except AttributeError :
            print(no_parking_lot_msg)
    elif task == 8:
        users_menu()


def test_menu():
    while True:
        if logged:
            print("1.open parking lot")
        else:
            print("1.log in")
        print("2.Add car to the parking lot\n"
              "3.Remove car from the parking lot\n"
              "4.Report of cars parked for more then 24H\n"
              "5.General report of cars in the parking lot")
        if logged:
            print("6.Change parking price\n"
                  "7.Change max parking spots\n"
                  "8.Uses management menu\n"
                  "9.Log out")
        print("0.Exit")
        try:
            task = int(input())
            if logged:
                # make sure the num is a valid option
                if task not in range(0, 10):
                    print("please pick a valid option\n")
                    continue
            else:
                # make sure the num is a valid option
                if task not in range(0, 6):
                    print("please pick a valid option\n")
                    continue
        except ValueError:
            print("can only input numbers\n")
            print("")
            continue
        task_test(task)


logged = False
lot_test = ""

if __name__ == "__main__":
    u = Users()
    u.add_user("admin", "admin")
    lot = ""
    logged_in = False
    # test to combine the menus in to 1 menu
    # test_menu()
    while True:
        if not logged_in:
            logged_in, lot = not_logged_menu(lot)
        else:
            logged_in, lot = logged_in_menu(lot)

