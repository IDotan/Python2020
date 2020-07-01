import os
import myTestTools
from slide15 import itai15

itai15.read_csv("test.csv")
if not myTestTools.print_test(itai15.delete_by_id, 123456789) == "The student was deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_id, 123456789) == "The given ID was not found":
    raise EOFError
itai15.read_csv("test.csv")
if not myTestTools.print_test(itai15.delete_by_id, 222222222) == "The student was deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_id, 222222222) == "The given ID was not found":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_id, 333333333) == "The student was deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_id, 333333333) == "The given ID was not found":
    raise EOFError
itai15.read_csv("test.csv")
if not myTestTools.print_test(itai15.delete_by_name, "Itai lol") == "The given name was not found":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "Itai 2nd") == "The student\\s been deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "Itai Dotan") == "The student\\s been deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "Itai Dotan") == "The given name was not found":
    raise EOFError
itai15.read_csv("test.csv")
if not myTestTools.print_test(itai15.delete_by_name, "afrat shany") == "The student\\s been deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "afrat shany") == "The given name was not found":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "bob boby") == "The student\\s been deleted":
    raise EOFError
if not myTestTools.print_test(itai15.delete_by_name, "bob boby") == "The given name was not found":
    raise EOFError
itai15.read_csv("test.csv")
print(itai15.students_list.is_empty())
itai15.delete_by_name("itai 2nd")
itai15.delete_by_id(123456789)
itai15.delete_by_name("afrat shany")
itai15.delete_by_name("bob boby")
print(itai15.students_list.is_empty())
if not os.path.exists("reports"):
    os.mkdir("reports")
itai15.read_csv("good.csv")
itai15.students_list.report_by_year_complete()
itai15.students_list.all_report()
itai15.read_csv("grades_reports.csv")
itai15.students_list.outstanding_report()
itai15.students_list.incorrect_status()



