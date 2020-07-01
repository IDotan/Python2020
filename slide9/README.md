### itai9.py - Mini projact
Script to control a parking lot, mange the free space, parked cars and payment.  
At start the following menu well be shown:  
1.	Create new parking lot. (available only with log in)
2.	Add car to the lot.
3.	Remove car from the lot
4.	Change parking hour cost. (available only with log in)
5.	Change max parking space. (available only with log in)
6.	Report of cars parked for more than 24 hours.
7.	Report of all cars in the lot.  
The 24 hours report will print car plate and phone number of the cars parked for more than 24 hours.  
The general report will print all cars car type(privet\public) and plate number.
#### Class to use
**Class car:**    
•	car plate, car type, entry time and phone number  
•	getters & setters.  
 **Class ParkingLot:**    
•	cars array, max space, pay per hour.  
•	getters & setters.  
•	Add and remove car.  
•	Print general report and 24 hours report.  
#### Rules 
1.	Can’t add 2 cars with the same plate number.
2.	Can’t add a car when the max space in the lot been reached.
3.	When removing a car there must be a print of the sum to pay.
#### Extra task/ challenges
1.	Options which need a log in will not be shown in the normal menu.
2.	Mange users, add remove and start with a default user.
3.	Adding user must be valid user and password with the rolls of slide 8. 
4. Can't add new user with the same ID as a registered user.
