from random import randint


def get_min(arr):
    # go over the arry to find the lowes number
    lengthe = len(arr)
    num = 10000
    for i in range(lengthe):
        if arr[i] < num:
            num = arr[i]
    return num


def get_max(arr):
    # go over the arry to find the highes number
    length = len(arr)
    num = 0
    for i in range(length):
        if arr[i] > num:
            num = arr[i]
    return num


def insert_value(arr, value):
    arr.append(value)


def remove_value(arr, value):
    # ask find_index if the number in the given array
    index = find_index(arr, value)
    # index = -1 when find_index did not find the number
    if index != -1:
        # clear the given array in the given index
        arr.pop(index[1])
    else:
        print("Number not in the array")


# sort the array, asc = True: Ascending, asc = False: Descending
def sort_array(arr, asc):
    new_arr = arr
    length = len(arr)
    # sort array in ascending order
    if asc == True:
        for i in range(length):
            for j in range(i):
                if new_arr[j] < new_arr[i]:
                    num1 = new_arr[j]
                    num2 = new_arr[i]
                    new_arr[i] = num1
                    new_arr[j] = num2
    else:
        for i in range(length):
            for j in range(i):
                if new_arr[j] > new_arr[i]:
                    num1 = arr[j]
                    num2 = arr[i]
                    new_arr[i] = num1
                    new_arr[j] = num2

    return new_arr


def count_value(arr, value):
    new_arr = arr
    lf = value
    dup = 0
    length = len(arr)
    for i in range(length):
        if new_arr[i] == lf:
            dup += 1
    return dup


def find_index(arr, value):
    # set index to be -1 to send if the number was not found, send index = 1 if the number is found
    index = -1
    # go over the array to look for the given number
    length = len(arr)
    for i in range(length):
        if arr[i] == value:
            index = i
    return index


def arr_avg(arr):
    length = len(arr)
    sum = 0
    elm = 0
    # go over the array sum the numbers and divide by number of elements in the array
    for i in range(length):
        sum += arr[i]
        elm += 1
    avg = sum / elm
    return avg


def find_missing_values():
    # did and used find_index
    # if i must creat this function let me know
    pass


def duplicaits(arr):
    new_arr = arr
    dup_list = []
    length = len(new_arr)
    for i in range(length):
        j = i + 1
        while j < length:
            if new_arr[i] == new_arr[j]:
                dup = new_arr.pop(j)
                dup_list.append(dup)
                length = len(new_arr)
            j += 1
    return dup_list


def create_random_array(array_size):
    random_array = []
    size = array_size
    # go space by space in the new arry to fill with randum_num
    for i in range(size):
        random_array.append(randum_num())
    return random_array


# get a randome number
def randum_num():
    num = randint(0, 10000)
    return num


def menu():
    arr = []
    arr = create_random_array(10)
    print(arr)
    task = int(input("please selcet action:\n"
                     "1.show Min and Max number in the array\n"
                     "2.Add or remove of numbers\n"
                     "3.sort the array from low to high or high to low\n"
                     "4.show the average of the numbers in the array\n"
                     "5.Find number position in the array\n"
                     "6.Find number of times a number index in the arry\n"
                     "7.Find duplicates numbers\n"
                     "8.Find missing numbers\n"
                     "9.Clear array and create new arry with 500 random numbers\n"))
    if task == 1:
        print("Min : " + str(get_min(arr)) + "\nMax : " + str(get_max(arr)) + "\n")
    elif task == 2:
        subtask = int(input("1.Remove\n"
                            "2.Add\n"))
        if subtask == 1:
            num = int(input("What number do you want to remove?\n"))
            remove_value(arr, num)
            print(arr)
        elif subtask == 2:
            num = int(input("What number do you want to Add?\n"))
            insert_value(arr, num)
            print(arr)
        else:
            return
    elif task == 3:
        subtask = int(input("1.Sort form top to bottom\n"
                            "2.Sort from botom to top\n"))
        if subtask == 1:
            new_arr = sort_array(arr, False)

        elif subtask == 2:
            new_arr = sort_array(arr, True)
        print(new_arr)

    elif task == 4:
        print("The average is :" + str(arr_avg(arr)))
    elif task == 5:
        num = int(input("What number's index to you want to find?\n"))
        index = find_index(arr, num)
        if index != -1:
            print("You'r number index is :" + str(index))
        else:
            print("You'r number is not in the array")

    elif task == 6:
        num = int(input("Witch number do you want to know the times of duplications??\n"))
        isit = count_value(arr, num)
        if isit != 0:
            print("You'r number showed up in the array " + str(isit) + " time\s")
        else:
            print("You'r number was not in the array")
    elif task == 7:
        dup_list = duplicaits(arr)
        if len(dup_list) != 0:
            print(dup_list)
        else:
            print("No duplicaits where found")
    elif task == 8:
        miss = int(input("What number are you looking for?\n"))
        index = find_index(arr, miss)
        if index != -1:
            print(str(miss) + " was found in the array")
        else:
            print(str(miss) + " was not in your array")
    elif task == 9:
        create_random_array(500)
    else:
        return


menu()
# create_random_array(50)
