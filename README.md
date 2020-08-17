# Pangram
### Aim:
Write a program that checks wether a given string is a **Pangram** or not.

### Procedure:
Step 1 : Create a list *l* which contains all the lower case alphabets.\
Step 2 : Declare an empty list *q*.\
Step 3 : Input a string and store it in *sentence*.\
Step 4 : As our list l contains all lower case alphabets convert *sentence* into lower case by using lower() function.\
Step 5 : Take a for loop which iterates along the universal list *l*.\
Step 6 : And if i is in *sentence* then we append the value of i into the declared string *q*.\
Step 7 : And if the list *q* == list *l* it is a **Pangram**.\
Step 8 : Else it is not a pangram.\
### Output And Analysis:
sentence = "abcdefghijklmnopqrstuvwxyz"\
**Output** = It is a Pangram\
sentence = "My name is Chaitanya"\
**Output** = It isn not a Pangram\
