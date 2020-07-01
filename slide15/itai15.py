import csv
import os
import shutil
import time

"""
code to mange students data
"""
current_year = time.struct_time(time.localtime())[0]


class Node:
    """
    | class Node to use in the LinkedList
    """

    def __init__(self, data, next=None):
        """
        | create a new Node
        :param data: the data of the new node
        :param next: the next of the node, default none
        """
        self.__data = data
        self.__next = next

    def get_data(self):
        """
        | get the data of the node
        :return: the data of the node
        """
        return self.__data

    def get_next(self):
        """
        | get the next of the node
        :return: the next of the node
        """
        return self.__next

    def set_data(self, data):
        """
        | set new data to the given node
        :param data: the data to set in the node
        """
        self.__data = data

    def set_next(self, next):
        """
        | set the next of the given node
        :param next: the next to set to
        """
        self.__next = next


class LinkedList:
    """
    | class of a linked list of node elements
    """

    def __init__(self, data):
        """
        | create new linked list
        :param data: the data at the start of the list
        """
        self.head = Node(data)

    def print_all(self):
        """
        | print all the data of all nodes in the list
        """
        temp = self.head
        # go over the list to print each entry
        while temp:
            print(temp.get_data())
            # set temp to the next entry to move forward
            temp = temp.get_next()

    def add_at_end(self, data):
        """
        | add a new node at the end of the list
        :param data: the data to be added at the end of the list
        """
        temp = self.head
        # go over the list to find the last entry
        while temp:
            if temp.get_next() is None:
                temp.set_next(Node(data))
                break
            # set temp to the next entry to move forward
            temp = temp.get_next()

    def count_list(self):
        """
        | count the numbers of node elements in the list
        :return: int of the number of elements
        """
        temp = self.head
        # set the count to 0
        count = 0
        # go over the list to count the number of nodes in it
        while temp:
            # add 1 to the count
            count += 1
            # set temp to the next entry to move forward
            temp = temp.get_next()
        return count

    def add_at_start(self, data):
        """
        | add new node at the start of the list
        :param data: the data of the node
        """
        # save the old head
        old_head = self.head
        # change to the new head
        self.head = Node(data)
        # set the next of the new head to the old head
        self.head.set_next(old_head)

    def delete_by_id(self, search_id):
        """
        | search for the given id in the list and delete it
        :param search_id: the id to be looked for
        :return: True when the id was deleted, False when not found
        """
        temp = self.head
        # check if we want to delete the head of the list
        if temp.get_data().get_data().get_id() == search_id:
            # set the head of the list to the next of the old head
            self.head = temp.get_next()
            return True
        else:
            # go over the list to find the student to delete
            while temp.get_next():
                # check if the student is found at the given node
                if temp.get_next().get_data().get_data().get_id() == search_id:
                    # change the next of the node we are at to the one after its next
                    temp.set_next(temp.get_next().get_next())
                    return True
                    # set temp to the next entry to move forward
                temp = temp.get_next()
                if temp is None:
                    break
            return False

    def delete_by_name(self, first, last):
        """
        | search for the given first and last name in the list and delete it
        :param first: the first name of the student to delete
        :param last: the last name of the student to delete
        :return: True when the id was deleted, False when not found
        """
        del_count = 0
        temp = self.head
        # check if we want to delete the head of the list
        if temp.get_data().get_data().get_first_name().lower().replace("-", " ") == first and \
                temp.get_data().get_data().get_last_name().lower().replace("-", " ") == last:
            # set the head of the list to the next of the old head
            self.head = temp.get_next()
            del_count += 1
        else:
            # go over the list to find the student to delete
            while temp.get_next():
                # check if the student is found at the given node
                if temp.get_next().get_data().get_data().get_first_name().lower().replace("-", " ") == first:
                    # when the first name is fount check if the last name is a match
                    if temp.get_next().get_data().get_data().get_last_name().lower().replace("-", " ") == last:
                        # change the next of the node we are at to the one after its next
                        temp.set_next(temp.get_next().get_next())
                        del_count += 1
                temp = temp.get_next()
                if temp is None:
                    break
        if del_count != 0:
            return True
        return False

    def add_after(self, after, data):
        """
        | add new node after given data
        :param after: the data to be before
        :param data: the data to add in the list
        """
        temp = self.head
        while temp:
            # check if the after match the node in the list
            if temp.get_data() == after:
                # keep the old next of the node in the list
                old_next = temp.get_next()
                # set the next of the node to the node we added witch will have its next point to the old next
                temp.set_next(Node(data, old_next))
            # set temp to the next entry to move forward
            temp = temp.get_next()

    def is_empty(self):
        """
        | check if the list is empty
        :return: True when empty
        """
        if self.head is None:
            return True
        elif self.head.get_data() is None:
            return True
        else:
            return False

    def report_by_year_temp(self):
        """
        | aid function to "report_by_year_complete"
        | go over the student list and split it to usable csv files
        """
        temp = self.head
        # create the temp folder for the csv files
        if not os.path.exists("temp_reports_csv"):
            os.mkdir("temp_reports_csv")
        # go over the student list
        while temp:
            # get the needed info
            temp_info = get_report_info(temp)
            # write the info to the year csv file
            with open("temp_reports_csv\\" + str(temp_info[7]) + ".csv", "a") as temp_csv:
                temp_csv.write(f"{temp_info[0]},{temp_info[1]},{temp_info[2]},{temp_info[3]},{temp_info[5]}\n")
            # set temp to the next entry to move forward
            temp = temp.get_next()

    def report_by_year_complete(self):
        """
        | create a report by year to 'reports' folder.
        | every year in its on file, 'year.txt'
        """
        # create the csv to work with
        self.report_by_year_temp()
        # get all the csv files to go over
        temp_reports = os.listdir("temp_reports_csv")
        for i in temp_reports:
            temp_count, temp_math, temp_prog = 0, 0, 0
            # open new file report for the year
            with open("reports\\" + i[slice(-4)] + ".txt", "w") as this_txt:
                # open and go over the given CSV file
                with open("temp_reports_csv\\" + i, newline='') as csv_file:
                    reader = csv.reader(csv_file, delimiter=',')
                    for row in reader:
                        this_math = int(row[2])
                        this_prog = int(row[3])
                        # write the info in to the report
                        this_txt.write(f"{row[0]} {row[1]} ID: {str(row[4])} "
                                       f"average: {(this_math + this_prog) / 2}\n")
                        # add to the yearly count
                        temp_count += 1
                        temp_math += this_math
                        temp_prog += this_prog
                # add the summary off the year
                this_txt.write((f"The averages are - over all: {(temp_math + temp_prog) / (temp_count * 2)}, "
                                f"math: {temp_math / temp_count}, programing: {temp_prog / temp_count}"))
        # force delete the temp csv files folder
        shutil.rmtree('temp_reports_csv', ignore_errors=True)

    def all_report(self):
        """
        | create a report of all the students
        """
        with open("reports\\All.txt", 'w') as report:
            temp = self.head
            count, avg_math, avg_prog = 0, 0, 0
            # go over the list to print each entry
            while temp:
                # get the student info
                temp_info = get_report_info(temp)
                # format and write the student info
                temp_student = f"{temp_info[0]} {temp_info[1]} " \
                               f"ID: {temp_info[5]} average: {temp_info[4]}\n"
                report.write(temp_student)
                # add to the over all average
                count += 1
                avg_math += temp_info[2]
                avg_prog += temp_info[3]
                # set temp to the next entry to move forward
                temp = temp.get_next()
            # add the sum line of the report
            report.write(f"The averages are - over all: {(avg_math + avg_prog) / (count * 2)}, "
                         f"math: {avg_math / count}, programing: {avg_prog / count}")

    def outstanding_report(self):
        """
        | create a report of all the outstanding students
        | outstanding student = programing grade >= 90 & average grade >= 85
        """
        with open("reports\\outstanding.txt", 'w') as report:
            temp = self.head
            while temp:
                # get the student info
                temp_info = get_report_info(temp)
                if temp_info[3] >= 90 and temp_info[4] >= 85:
                    report.write(f"{temp_info[0]} {temp_info[1]} average: {temp_info[4]}\n")
                # set temp to the next entry to move forward
                temp = temp.get_next()

    def incorrect_status(self):
        """
        | create a report of all the student with incorrect academic status
        | incorrect status = average < 70 or (math < 60 and programing < 70)
        """
        with open("reports\\incorrect.txt", 'w') as report:
            temp = self.head
            while temp:
                # get the student info
                temp_info = get_report_info(temp)
                if temp_info[4] < 70 or (temp_info[2] < 60 and temp_info[3] < 70):
                    report.write(f"{temp_info[0]} {temp_info[1]} average: {temp_info[4]}\n")
                # set temp to the next entry to move forward
                temp = temp.get_next()

    def save_to_csv(self, csv_file_to_save_to):
        """
        | save to student list data to a csv file
        :param csv_file_to_save_to: name to give to the csv file
        """
        try:
            with open(csv_file_to_save_to, 'w') as save_file:
                temp = self.head
                while temp:
                    # get the student info
                    temp_info = get_report_info(temp)
                    save_file.write(f"{temp_info[0]},{temp_info[1]},{temp_info[5]},"
                                    f"{temp_info[2]},{temp_info[3]},{temp_info[7]},{temp_info[6]}\n")
                    temp = temp.get_next()
            print("Save complete\n")
        except PermissionError:
            print("the file is protected\n")


class Student:
    """
    | class of student information
    """

    def __init__(self, first_name="unnamed", last_name="unnamed", id_num=-1, math_grade=-1,
                 programing_grade=-1, year=-1, prep=-1):
        """
        | create new student object
        | first and last name default "unnamed"
        | rest of the parameters have a default of (-1)
        :param first_name: student's first name
        :param last_name: student's last name
        :param id_num: student's ID number
        :param math_grade: student's average math grade
        :param programing_grade: student's average programing grad
        :param year: the year
        :param prep: 0 - didn't do preparatory program. 1 - did do  preparatory program
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_num = id_num
        self.__math_grade = math_grade
        self.__programing_grade = programing_grade
        self.__year = year
        self.__prep = prep

    def get_first_name(self):
        """
        | get the first name of the student
        :return: string of the first name
        """
        return self.__first_name

    def get_last_name(self):
        """
        | get the last name of the student
        :return: string of the last name
        """
        return self.__last_name

    def get_id(self):
        """
        | get the student's ID number
        :return: int of the ID
        """
        return int(self.__id_num)

    def get_math(self):
        """
        | get the student's math grade
        :return: int of the math grade
        """
        return int(self.__math_grade)

    def get_programing_grade(self):
        """
        | get the student's programing grade
        :return: int of the programing grade
        """
        return int(self.__programing_grade)

    def get_year(self):
        """
        | get the student's year of studding
        :return: int of the year
        """
        return int(self.__year)

    def get_prep(self):
        """
        | get the student's preparatory program status
        :return: int of the student's status
        """
        return int(self.__prep)


def get_report_info(temp):
    """
    | get info of the given student node for the reports
    :param temp: the node of the student
    :return: 0-first name, 1-last name, 2-math, 3-programing, 4-average, 5-id, 6-prep, 7-year
    """
    # get the students grades
    temp_math = temp.get_data().get_data().get_math()
    temp_prog = temp.get_data().get_data().get_programing_grade()
    # average the grades
    temp_avg = (temp_math + temp_prog) / 2
    # get the student's name
    temp_first = temp.get_data().get_data().get_first_name()
    temp_last = temp.get_data().get_data().get_last_name()
    # get the student's id
    temp_id = temp.get_data().get_data().get_id()
    # get the student's preparatory program status
    temp_prep = temp.get_data().get_data().get_prep()
    temp_year = temp.get_data().get_data().get_year()
    return temp_first, temp_last, temp_math, temp_prog, temp_avg, temp_id, temp_prep, temp_year


def get_name(which_name):
    """
    | get student name from the user
    :param which_name: first or last name
    :return: string of the name
    """
    name = input(f"Please enter the students {which_name} name:\n")
    if "" == name:
        # when the input is not valid print and recall
        print("can't leave empty")
        get_name(which_name)
    if " " in name:
        # when the input is not valid print and recall
        print("can't have spaces")
        get_name(which_name)
    return name


def get_id():
    """
    | get the student id from the user
    :return: the students ID
    """
    try:
        stud_id = (input("Please enter student's ID:\n"))
        check, msg = check_id(stud_id)
        if not check:
            # when the input is not valid print and recall
            print(msg)
            get_id()
        return int(stud_id)
    except ValueError:
        # when the input is not valid print and recall
        print("can only inout integers")
        get_id()


def check_id(id_to_check):
    """
    | check if the given id is valid
    :param id_to_check: the id to check
    :return: True, "" - when true. False, message - when false
    """
    if "" == str(id_to_check):
        return False, "can't leave empty\n"
    if " " in str(id_to_check):
        return False, "can't have spaces\n"
    if not len(str(id_to_check)) == 9:
        return False, "the ID must have 9 numbers in it\n"
    if id_to_check == "000000000":
        return False, "can't have an ID of only 0's"
    # when all check are fine return true
    return True, ""


def get_grade(which_grade):
    """
    | get the grade of the student from the user
    :param which_grade: math grade or programing grade
    :return: the students grade
    """
    try:
        grade = int(input(f"Please enter student's {which_grade} grade:\n"))
        if not 0 <= grade <= 100:
            # when the input is not valid print and recall
            print("the grade can only be between 0-100")
            get_grade(which_grade)
        return grade
    except ValueError:
        # when the input is not valid print and recall
        print("can only use integers")
        get_grade(which_grade)


def get_year():
    """
    | get the student's study year
    :return: the year
    """
    try:
        year = input("Please enter the year the student study in:\n")
        if not len(year) == 4:
            # when the input is not valid print and recall
            print("the input must be in 'yyyy' format")
            get_year()
        year = int(year)
        if not 1990 <= year <= (current_year + 2):
            # when the input is not valid print and recall
            print(f"the year can only be between 1990-{current_year + 2}")
            get_year()
        return year
    except TypeError:
        # when the input is not valid print and recall
        print("can only use integers")
        get_year()
    except ValueError:
        # when the input is not valid print and recall
        print("can only use integers")
        get_year()


def get_prep():
    """
    | get if the student been to a preparatory program
    :return: 1- student was in preparatory program 0- if not
    """
    prep = input("Did the student been to a preparatory program?\n"
                 "y/n\n")
    # format to lower to prevent a miss read
    prep = prep.lower()
    if prep == "y" or prep == "yes":
        return 1
    elif prep == "n" or prep == "no":
        return 0
    else:
        # when the input is not valid print and recall
        print("please type in only y/n, yes/no")
        get_prep()


def get_student_info():
    """
    | get the info of the student
    :return: list of the student info
    """
    data_list = []
    # get and add first name
    temp = get_name("first")
    data_list.append(temp)
    # get and add last name
    temp = get_name("last")
    data_list.append(temp)
    # get and add ID
    temp = get_id()
    data_list.append(temp)
    # get and add math grade
    temp = get_grade("math")
    data_list.append(temp)
    # get and add programing grade
    temp = get_grade("programing")
    data_list.append(temp)
    # get and add the year
    temp = get_year()
    data_list.append(temp)
    # get and add preparatory program status
    temp = get_prep()
    data_list.append(temp)
    return data_list


def add_student():
    """
    | add new student to the list of students
    """
    # go and ask for the info from the user
    student = Student(*get_student_info())
    # check if the list is empty
    if students_list.is_empty():
        # add at the start of the list
        add_data_to_list(student, True)
    else:
        # add at the end of the list
        add_data_to_list(student, False)


def delete_by_id(id_delete):
    """
    | delete student by the ID number
    :param id_delete: the id to find and delete by
    """
    # check if the id is valid
    check, msg = check_id(id_delete)
    if not check:
        print(msg)
        # go back when the input was unusable
        delete_student()
    deleted = students_list.delete_by_id(id_delete)
    # print when the delete action was successful
    if deleted:
        print("The student was deleted\n")
        return True
    else:
        print("The given ID was not found\n")
        return False


def delete_by_name(name):
    """
    | delete a user by first and last name
    :param name: string of the student first and last name
    """
    # make sure the input ois not empty
    if name == "":
        print("cant leave empty")
        # go back when when empty
        delete_student()
    try:
        # format the input to the needed format
        fname, lname = name.split()
        fname = fname.replace("-", " ")
        lname = lname.replace("-", " ")
    # when cant the input is not of 2 name and cant be used
    except ValueError:
        print("must have first and last name only")
        # go back when the input was unusable
        delete_student()
    # send the given names to be looked for and deleted
    deleted = students_list.delete_by_name(fname.lower(), lname.lower())
    # print when the delete action was successful
    if deleted:
        print("The student\\s been deleted\n")
        return True
    else:
        print("The given name was not found\n")
        return False


def delete_student():
    """
    | delete a student form the linked list
    """
    if students_list.is_empty():
        print("The student list is empty\n")
        return
    its_an_id = True
    # get the student to delete info from the user
    stud_del = input("Please enter the student name or ID to delete:\n"
                     "for 2 first/last name use '-', first-first last\n"
                     "0 to go back\n")
    # the user asked to go back to the menu
    if stud_del == "0":
        return
    try:
        # try to convert the input to int to check if its an ID
        stud_del = int(stud_del)
    # when cant be an int its by name
    except ValueError:
        # set to indicate its not by id
        its_an_id = False
    # do when it's an id
    if its_an_id:
        # send to delete
        delete_by_id(stud_del)
    # do when it's by name
    else:
        # send to delete
        delete_by_name(stud_del)


def delete_all_students():
    """
    | delete all the students from the linked list
    """
    global students_list
    students_list = LinkedList(None)
    print("All student data was deleted\n")


def report_folder_exists():
    """
    | check if 'reports' folder exists
    :return: True when exists
    """
    # check if the folder exists
    if os.path.exists("reports"):
        return True
    return False


def delete_reports_folder():
    """
    | delete the 'reports' folder
    """
    # check if the folder exists
    if not report_folder_exists():
        print("There is no 'reports' folder")
        return
    # when the folder exists
    try:
        os.rmdir("reports")
    # when the folder is not empty
    except OSError:
        delete_full_folder()


def delete_full_folder():
    """
    | function to confirm the delete of a full folder and the delete of the folder
    """
    # asks for confirmation of the deletion
    task = input("The folder is not empty, do you want to delete any why?\n"
                 "y/n\n")
    task = task.lower()
    if task == "y" or task == "yes":
        """
        # force delete of the folder
        shutil.rmtree('reports', ignore_errors=True)
        """
        # get list if all files in the folder
        files = os.listdir('reports')
        # go one by one and delete all the files in the folder
        for i in files:
            os.remove('reports\\' + i)
        # delete the folder when its emptied up
        os.rmdir("reports")
    elif task == "n" or task == "no":
        return
    else:
        # when the input is not valid print and recall
        print("please type in only y/n, yes/no")
        delete_full_folder()


def create_report_folder_if_needed():
    """
    | create reports folder when needed and it didn't exists before
    """
    if report_folder_exists():
        return
    os.mkdir('reports')


def reports_menu():
    """
    | menu of the available reports to create
    """
    while True:
        try:
            task = int(input("Please pick what report you are looking for:\n"
                             "1.All students\n"
                             "2.Yearly reports\n"
                             "3.Outstanding Students\n"
                             "4.Academic status incorrect\n"
                             "0.Go back\n"))
        except ValueError:
            print("can only use an integer\n")
            continue
        if task not in range(0, 5):
            print("please pick a valid option\n")
        global students_list
        if task == 0:
            return
        if task == 1:
            create_report_folder_if_needed()
            students_list.all_report()
        if task == 2:
            create_report_folder_if_needed()
            students_list.report_by_year_complete()
        if task == 3:
            create_report_folder_if_needed()
            students_list.outstanding_report()
        if task == 4:
            create_report_folder_if_needed()
            students_list.incorrect_status()


def load_from_csv():
    """
    | import data from CSV file to the student list
    """
    # get the csv path\file
    print("Please enter the CSV file to load:\n"
          "0 To go back to menu")
    # get the csv path\file
    file = get_csv_file()
    if file == "0":
        return
    # send the file to be added
    load_from_csv_part_2(file)


def load_from_csv_part_2(file):
    """
    | continue of 'load_from_csv'
    | check the list status and send the csv to be loaded
    :param file: the csv file to load
    """
    try:
        # check if the list is empty
        if students_list.is_empty():
            read_csv(file)
        # when the list is not empty send the data to be added at the end
        else:
            read_csv(file, False)
    except FileNotFoundError:
        # when the file is not valid print and recall
        print("The file was unreachable, please try again\n")
        load_from_csv()


def export_overwrite_check(file):
    """
    | when the file exists ask the user if to overwrite it
    :param file: the file name to ask about
    """
    do = input(f"The file '{file}' already exists\n"
               f"Do you wish to overwrite it? y/n\n")
    # overwrite the file
    if do.lower() == 'y' or do.lower() == 'yes':
        students_list.save_to_csv(file)
    # go back to pick a name
    elif do.lower() == 'n' or do.lower() == 'no':
        export_to_csv()
    else:
        # when the input is unusable print and recall
        print("please enter only y/n\n")
        export_to_csv()


def export_to_csv():
    """
    | save the student list to a CSV file
    :return: True when user want to go back
    """
    # ask for name of the file to save to
    print("Please enter the name to save to:\n"
          "0 To go back")
    try:
        # get the name
        file = get_csv_file()
        if file == '0':
            return True
        file = file + '.csv'
        # check if the file exists
        if not os.path.exists(file):
            # send to be saved to csv
            students_list.save_to_csv(file)
        else:
            # ask the user what to do when to file exists
            export_overwrite_check(file)
    # when the input is unusable print and recall
    except ValueError as e:
        print(e)
        export_to_csv()
    except FileNotFoundError:
        print("unreachable path for the file\n")
        export_to_csv()
    except OSError:
        print("Illegal character was used, please try again\n")
        export_to_csv()


def exit_code():
    """
    | confirm action on exit
    """
    # when the list is empty exit
    if students_list.is_empty():
        exit()
    # when there is data ask the user if he wants to save
    task = input("Do you want to save your work? y/n\n")
    if task.lower() == 'y' or task.lower() == 'yes':
        back_to_menu = export_to_csv()
        if back_to_menu:
            return
        exit()
    # go back to pick a name
    elif task.lower() == 'n' or task.lower() == 'no':
        exit()
    else:
        # when the input is unusable print and recall
        print("please enter only y/n\n")
        exit_code()


def menu():
    """
    | menu to show to the user
    """
    while True:
        try:
            task = int(input("1.Add new student\n"
                             "2.Delete student\n"
                             "3.Delete all students\n"
                             "4.Delete reports folder\n"
                             "5.Reports menu\n"
                             "6.Load students from CSV file\n"
                             "7.Export students to CSV file\n"
                             "0.Exit\n"))
        except ValueError:
            print("can only use an integer\n")
            continue
        if task not in range(0, 8):
            print("please pick a valid option\n")
        if task == 1:
            add_student()
        elif task == 2:
            delete_student()
        elif task == 3:
            delete_all_students()
        elif task == 4:
            delete_reports_folder()
        elif task == 5:
            # make sure there is data to report on
            if not students_list.is_empty():
                reports_menu()
            else:
                print("The student list is empty\n")
        elif task == 6:
            load_from_csv()
        elif task == 7:
            # make sure there is data to save
            if not students_list.is_empty():
                export_to_csv()
            else:
                print("The student list is empty\n")
        elif task == 0:
            exit_code()


def check_csv_row(row):
    """
    | check if any of the row input is empty
    | change any empty index to defaults value
    | row[index] index = 0-1 - default "unnamed"
    | row[index] index = 2-6 - default (-1)
    :param row:  row to be checked
    :return: the row after checked and corrected
    """
    # check to row is at a usable length
    if not len(row) == 7:
        raise TypeError
    temp_index = 0
    # go over the row and check its info
    for i in row:
        # when its the 2 first index an they are empty
        if temp_index < 2 and len(i) == 0:
            row[temp_index] = "unnamed"
        # when its the other index an its empty
        elif temp_index > 1 and len(i) == 0:
            row[temp_index] = -1
        temp_index += 1
    return row


def read_csv(path, first=True):
    """
    | read the CSV file and add it's data to the list
    :param path: the path of the file to read from
    :param first: True for new list, False add at the end.
    """
    # create and close an error.txt damp file to be used
    create = open("error.txt", 'w')
    create.close()
    # open and go over the given CSV file
    with open(path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            try:
                # check the row and convert it to a Student object
                row = check_csv_row(row)
                temp = Student(*row)
                if first:
                    # send to be added
                    add_data_to_list(temp, first)
                    # change to show its no longer the first
                    first = False
                else:
                    # send to be added
                    add_data_to_list(temp, first)
            # when the given data is unusable damp it to error.txt file
            except ValueError:
                with open("error.txt", 'a') as error:
                    error.write(str(row) + "\n")
            except TypeError:
                with open("error.txt", 'a') as error:
                    error.write(str(row) + "\n")
    # clear the error.txt damp when there where no errors
    delete_empty_error_damp()


def delete_empty_error_damp():
    """
    | delete the error.txt file damp when its empty
    """
    # open the file and read it
    temp = open("error.txt", 'r')
    no_error = temp.read()
    temp.close()
    # check if the file is empty
    if no_error == "":
        os.remove("error.txt")


def add_data_to_list(data, first):
    """
    | add the data to the student's list
    :param data: the data to add, list
    :param first: True for new list, False add at the end
    """
    global students_list
    # create new node with the data
    temp_node = Node(data)
    # do when its the first data in the list
    if first:
        students_list = LinkedList(temp_node)
    # when its any consecutive data in the list
    else:
        students_list.add_at_end(temp_node)


def get_csv_file():
    """
    | get the csv file from the user
    :return: the csv file path
    """
    file = input()
    # make sure not empty
    if "" == file:
        raise ValueError("Cant stay empty\n")
    return file


def boot():
    """
    | at boot ask for an exiting existing CSV file or start form scratch
    """
    global students_list
    while True:
        print("Please enter the CSV file you want to use\n"
              "Type \"none\" to start for scratch")
        try:
            task = get_csv_file()
        except ValueError as e:
            print(e)
            continue
        # create new and empty linked list
        if task.lower() == "none":
            # when the input is 'none' continue to the menu with the empty list
            students_list = LinkedList(None)
            menu()
            break
        # when a file was given
        else:
            try:
                # send to open and add the data
                read_csv(task)
                menu()
                break
            except FileNotFoundError:
                print("The file was unreachable, please try again\n")
                continue
            except OSError:
                print("Illegal character was used, please try again\n")
                continue


# globals to use in the code
students_list = LinkedList(None)

if __name__ == "__main__":
    boot()
