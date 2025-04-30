# in memory key value database with transactions

## how to run the code

1. make sure python 3 is installed, i currently have python 3.13.3 installed
2. run `py testDb.py` from the terminal in this project directory  
   - install python from https://www.python.org/

this will run the example tests described in the assignment and demonstrate how `put`, `get`, `begin_transaction`, `commit`, and `rollback` work

## recommended improvements for future assignment

In order to improve this assignment as an official course task, include a required test suite with expected outputs so grading can be automated allow optional bonus points for supporting nested transactions. Clarify in the assignment that only one transaction can run at a time and all uncommitted values should be invisible. Additionally suggest specifying error messages or custom exceptions to standardize behavior. 