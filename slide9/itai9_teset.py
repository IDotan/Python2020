from Slide9 import itai9
import time
import myTestTools

t1 = time.localtime(time.mktime(time.localtime()) - 86400)  # 24H back
c1 = itai9.Car(t1, "12-34-56", "private", "03-1234567")
t2 = time.localtime(time.mktime(time.localtime()) - 10800)  # 3H back
c2 = itai9.Car(t2, "88-88-22", "private", "03-1234567")
c3 = itai9.Car(time.localtime(), "88-88-33", "private", "03-5363783")
if not (c1.get_tel()) == "03-1234567":
    raise EOFError
c1.set_tel("123456")
if not c1.get_tel() == "123456":
    raise EOFError
if not (c1.get_v_type()) == "private":
    raise EOFError
try:
    c1.set_v_type("lol")
except TypeError as e:
    if not str(e) == "not a valid vehicle type":
        raise EOFError
c1.set_v_type("Private")
if not (c1.get_v_type()) == "private":
    raise EOFError
c1.set_v_type("Public")
if not (c1.get_v_type()) == "public":
    raise EOFError
if not (c1.get_plate()) == "12-34-56":
    raise EOFError
c1.set_plate("88-88-11")
if not (c1.get_plate()) == "88-88-11":
    raise EOFError
lot = itai9.ParkingLot()
lot + c1
lot + c2
if not myTestTools.print_test(lot.general_report) == "Total of 2 car\s, 1 private vehicle\s and 1 public vehicle\s :" \
                                       "\n1.public, plate number: 88-88-11" \
                                       "\n2.private, plate number: 88-88-22":
    raise EOFError
lot - c2
if not myTestTools.print_test(lot.general_report) == "Total of 1 car\s, 0 private vehicle\s and 1 public vehicle\s :" \
                                       "\n1.public, plate number: 88-88-11":
    raise EOFError
lot + c2
if not myTestTools.print_test(lot.more_then_24h) == '1. plate: 88-88-11 phone: 123456':
    raise EOFError
lot - c1
if not myTestTools.print_test(lot.more_then_24h) == 'no car have been parked for more then 24H':
    raise EOFError
lot + c1
lot.set_max_space(2)
try:
    lot + c3
except IndexError as e:
    if not str(e) == 'no more room in the parking lot':
        raise EOFError
lot.set_max_space(3)
lot + c3

u = itai9.Users()
u.add_user("Admin", "Admin")
try:
    u.remove_user("admin")
except ValueError as e:
    if not str(e) == "ID: 'admin' is not in the system":
        raise EOFError
# itai9.remove_car(lot)

