### The first few codes of the course
my few first codes in python. not to polished or complex.  
Here more for the record then to be shown, but feel free to do so.  

### itai5.py - Array handling  
Create a number array control script.  
When the program starts a menu with the following option will be shown:  
  1. Show min and max values.  
  2. Add and remove values.  
  3. Ascending or descending arranging of the array.  
  4. Calcolate average of the array.  
  5. Find value index.  
  6. Find and count value duplications.  
  7. Find missing values.  
  8. Delete all values.  
  9. Enter 500 random values.  
  
  **note:** can't use or import any thing out side of the written code

### itai6.py - Password generator  
Script to generate a password by the user specifications from a characters string using flags.  
Every flag represent a characters group then pick one from the group randomly, and add to the generated password.  
At the start of the script shows a menu to ask the user for the password parameters:
1.	Length.  
2.	What characters to include- capital , lower, numbers and symbols.

### itai7 - Working with dictionaries and Password ranking
This was one task i split to 2 script afterword for convenient.  
**note:** this 2 script use in code doctests witch may make it look long and a bit harder to read.
#### itai7_a.py - dictionaries handling
Create script to calculate the cost of a bakery next day missing ingredients using dictionaries. 
The script output will be a print of the costs for the next day, and of the ingredients there is more then needed to the next day if any.  
The script gets 3 dictionaries:  
  1.	The ingredients the bakery have.  
  2.	The ingredients the bakery need for the next day.  
  3.	The cost of the ingredients.  

**note:** the 2 last doctest in this script are meant to fail.
#### itai7_b.py - Password ranking
Script to verify passwords legitime, and rank its strength by the following criterions:  
Legitime:
1.	Must be longer than 4.
2.	Not include spaces.
3.	The use name is not in the password

Strength values:
1.	Length < 6, 1 point. 6 <= Length <= 8, 2 points. Length > 8, 3 points.
2.	Includes: upper 1 point, lower 1 point, numbers 1 point, symbols 2 points
3.	Includes mix of 2 char groups 1 extra point, more then 2 extra 3 points.

String rank:
1. rank <= 4, week.
2. 5 <= rank <= 6, fair.
3. rank == 7, strong
4. rank > 7, very strong.
