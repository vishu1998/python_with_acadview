import math  # IMPORTING MATH PACKAGE TO CALCULATE FACTORIAL OF NUMBER
def fact(no):   # FACT FUNCTION FOR CALCULATING FACTORIAL OF USER INPUT
    f = math.factorial(no)
    print(" FACTORIAL OF", no, " =", f)

var = int(input("ENTER THE NUMBER FOR WHICH YOU WANT TO CALCULATE FACTORAIL :"))

if var >= 0:    # CONDITION FOR POSITIVE NO
    fact(var)    # FUNCTION CALLING
else:           # IF USER GIVE INPUT AS A NEGATIVE THEN PRINT STATEMENT AND EXIT
    print("\nNEGATIVE NUMBER NOT ALLOWED")
    exit()