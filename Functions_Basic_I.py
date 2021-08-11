

#Excercise_1
def Excercise_1():
    def a():
        return 5
    print(a())
# Function a() return value 5. Value 5 is printed on the terminal

#Excercise_2
def Excercise_2():
    def a():
        return 5
    print(a()+a())
# Function a() return value 10. Value 10 is printed on the terminal

#Excercise_3
def Excercise_3():
    def a():
        return 5
        return 10
    print(a())
# Function a() return value 5. Value 5 is printed on the terminal. Second return statement is not considered.

#Excercise_4
def Excercise_4():
    def a():
        return 5
        print(10)
    print(a())
# Function a() return value 5. Value 5 is printed on the terminal. Stament "print(10)" in function a() is not executed because it is after the return statement

#Excercise_5
def Excercise_5():
    def a():
        print(5)
    x = a()
    print(x)
# Function a() does not return anything. It only print 5 on the terminal when is executed. Value of "x" is undefined. On terminal the values that are going to appear are 5 and "none"

#Excercise_6
def Excercise_6():
    def a(b,c):
        print(b+c)
    print(a(1,2) + a(2,3))
# Function a() does not return anything. It only print the sum of two given arguments on the terminal when is executed. On terminal the values that are going to appear are 3, 5 and an error. The last one is because python does not support the sum of two 'NoneType' variables

#Excercise_7
def Excercise_7():
    def a(b,c):
        return str(b)+str(c)
    print(a(2,5))
# Function a() return concatenation of two numbers converted to a string. On terminal the values that are going to appear is 25. 

#Excercise_8
def Excercise_8():
    def a():
        b = 100
        print(b)
        if b < 10:
            return 5
        else:
            return 10
        return 7
    print(a())
# Function a() return output of else statement (b>10) which is 10. On terminal the values that are going to appear are 100 and 10 (print(b) and print(a()) functions respectivetly). Third return statement (return 7) is not considered because it is after the other two return statements which are inside an if/else block

#Excercise_9
def Excercise_9():
    def a(b,c):
        if b<c:
            return 7
        else:
            return 14
        return 3
    print(a(2,3))
    print(a(5,3))
    print(a(2,3) + a(5,3))
# Function a() return the following outputs on for each statement called: 7 (a(2,3)) and 14 (a(5,3)). On terminal the values that are going to appear are 7 (print(a(2,3))), 14 (print(a(5,3))) and 21 (print(a(2,3))+print(a(5,3))). Third return statement (return 3) is not considered because it is after the other two return statements which are inside an if/else block

#Excercise 10
def Excercise_10():
    def a(b,c):
        return b+c
        return 10
    print(a(3,5))
# Function a() return the sum of two arguments. On terminal the value that is going to appear is 8 (print(a(3,5))). Second return statement (return 10) is not considered because it is after the first return statement (function finish when first return statement is run)

#Excercise 11
def Excercise_11():
    b = 500
    print(b)
    def a():
        b = 300
        print(b)
    print(b)
    a()
    print(b)
# Function a() does not return anything. On terminal the value that is going to appear are: 500 (first print(b) statement), 500(third print(b) statement),  and 300 (third print(b) statement isnisde a() function) and 500 (fourth print(b) statement). Function a() does not changes value of b variable outside function a().

#Excercise 12
def Excercise_12():
    b = 500
    print(b)
    def a():
        b = 300
        print(b)
        return b
    print(b)
    a()
    print(b)
# Function a() returns the value 300. On terminal the value that is going to appear are: 500 (first print(b) statement), 500(third print(b) statement),  and 300 (third print(b) statement isnisde a() function) and 500 (fourth print(b) statement). Function a() does not changes value of b variable outside function a().

#Excercise 13
def Excercise_13():
    b = 500
    print(b)
    def a():
        b = 300
        print(b)
        return b
    print(b)
    b=a()
    print(b)
# Function a() returns the value 300. On terminal the value that is going to appear are: 500 (first print(b) statement), 500(third print(b) statement),  and 300 (third print(b) statement isnisde a() function) and 300 (fourth print(b) statement). In this case, function a() changes the value of variable "b" in the line "b=a()", because a new value is being assigned.

#Excercise 14
def Excercise_14():
    def a():
        print(1)
        b()
        print(2)
    def b():
        print(3)
    a()
# Function a() and b() does not return anything. On terminal the value that is going to appear when function a() is being called are: 1, 3 and 2. Function b() is being called inside function a()

#Excercise 15
def Excercise_15():
    def a():
        print(1)
        x=b()
        print(x)
        return 10
    def b():
        print(3)
        return 5
    y = a()
    print(y)
# Function a() and b() return 10 and 5, respectivetly. On terminal the value that is going to appear when function a() is being called are: 1 (print(1) inside function a()), 3 (when calling function b() because line x=b() inside a() function), 5 (print(x)) and 10 (print(y)). Function b() is being called inside function a()
# ---------------------------------------------
# Run the function excercise to check the output here:
Excercise_15()


