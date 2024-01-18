# PYTHON AS FAST AS POSSIBLE

# DATA TYPES

    # int (whole integer)
         # 3

    # float (anything w decimals)
        # 2.5

    # string (anything in single or double quote marks)
         # "hello" / 'hello'

    # bool (one of two values, true or false)
        # True 1
        # False 0

# OUTPUT AND PRINTING
    # print("Hello mfers!")
    # print(4.5, "Hello peepz", 3.7, "halla", 5.5651354, "breh", True, False, end="/n")
    # print("halla")

# VARIABLES (reading top to bottom)
    # a = "1"
    # b = "2"
    # b = a
    # b = "3"
    # print(a, b)

    # halla_breh = "1"
    # print(halla_breh)

# INPUT
    # age = input("What is your age? ")
    # height = input("How tall are you in cms? ")
    # weight = input("How much do you weigh in kgs? ")
    # print("Hello sir, your age is", age, "and your are", height, "cms tall. I've also heard you're sitting at", weight,"kgs.")

# ARITHMATIC OPERATIONS
    # x = 9
    # y = 3
    # result1 = x / y
    # print(result1)
    # print(int(result1))

    # a = 2
    # b = 4
    # result2 = a ** b
    # print(result2)

    # x1 = 10
    # x2 = 3
    # result3 = x1 // x2
    # print(result3)
    # result4 = x1 / x2
    # print(result3)

    # a = 10
    # b = 3
    # result = (a % b) * 2
    # print(result)

    # num = input("number: ")
    # # num is variable, but input generates a "string" -> cannot add a "string" and int, convert string to int and all good
    # print(int(num) - 5)

    # num = input("number: ")
    # print(float(num)-5)

# STRING METHODS
    # hello = "hello"
    # print(type(hello))

    # hello = "hello".upper()
    # print(hello)
    # hello = "HELLO".lower()
    # print(hello)
    # hello = "HELLO"
    # print(hello.lower())

    # hello = "heLLo"
    # print(hello.upper())

    # hello = "heLLo MfErS"
    # print(hello.capitalize())

    # halla = "halla brehha"
    # print(halla.count("ll"))
    # halla = "halla brehha"
    # print(halla.count("HH".lower()))

    # hello = "heLLo World"
    # print(hello.upper().count("LL"))

    # x = "hello"
    # y = round(3.9)
    # print(x * y)

    # a = ("hello")
    # b = "brethren"
    # print(a + b)


# CONDITIONAL OPERATORS
    # ==
    # !=
    # <=
    # >=
    # <
    # >

    # x = "hello"
    # y = "hello"
    # print(x != y)
    #
    # x = "hello"
    # y = "hello"
    # print(x >= y)

    # x = "hello"
    # y = "helLo"
    # print(x != y)

    # # ordinal values ( ord() )
    # print("a" > "Z")
    # print(ord("a"))
    # print(ord("Z"))
    # print("a" > "b")
    # print(ord("a"))
    # print(ord("b"))

    # print(7.0 == 7)

    # result = 6 == 6
    # print(result)

# CHAINED CONDITIONS (TRICKY - REVIEW!)
    # x = 7
    # y = 8
    # z = 0
    # result1 = x == y
    # result2 = y > x
    # result3 = z < x + 2
    # # print(result1)
    # # print(result2)
    # # print(result3)
    #
    # # if result1, result2 OR result3 is true = print true
    # # result4 = result1 or result2 or result3
    # # print(result4)
    #
    # result4 = result1 or not result2 or result3
    # print(result4)
    #
    # print(not False)
    #
    # print(not (False or True))

# IF (first one, only one) / ELIF (must be after IF and before ELSE, inf many) / ELSE (last one, only one)
    # x = input("Name: ")
    # if x == "Mattias":
    #     print("There is only one.")
    # elif x == "Dan":
    #     print("F off Danny")
    # elif x == "Ben":
    #     print("Gimme back Matty!")
    # else:
    #     print("Where did Matty go?")

# COLLECTIONS (ordered/unordered group of elements (some data type: int, float, string, bool))
    # LIST (ordered collection, order matters)
        # x = [100, 99.9, "Mattias", True, False]
        # y = "Ben"
        # z = "Venkatanarasimharaju"
        # print(len(x), len(y), len(z))

        # x = [100, 99.9, "Mattias", True, False]
        # # add single element to end of list
        # x.append("lol")
        # # add multiple elements to list
        # x.extend([1,2,3])
        # print(x)

        # x = [100, 99.9, "Mattias", True, False]
        # y = "Halla"
        # x.append("lol")
        # x.extend([1,2,3])
        # print(x)

        # print(x.pop())
        # print(x)

        # print(x.pop(2))

        # print(x[2])
        # print(x[3])

        # Lists are mutable and items (data types) can be changed.
        # x[0] = "Mattias"
        # print(x)

        # x = [4, True, "hi"]
        # y = x
        # x[0] = "hello"
        # print(x,y)

    # TUPLES (immutable, cannot be changed)
        # x = (0,0,2,2)
        # x.append("lol")
        # print(x[0])

# FOR LOOPS (iterate a set nr of times)
    # range(): (stop), (start, stop), (start, stop, step)
        # for i in range(10, -1, -1):
        #     print(i)

        # x = [3,4,42,3,2,4]
        # for i in range(len(x)):
        #     print(x[i])

# WHILE LOOPS ("While condition == True:")
    # x = 0
    # while x < 10:
    #     print("run")
    #     x = x + 2

    # y = 0
    # while True:
    #     print("run")
    #     y = y + 1
    #     if y == 10:
    #         break

# SLICE OPERATOR ("slice = [start:stop:step]
    # x = [0,1,2,3,4,5,6,7,8]
    # sliced = x[0:4:2]
    # print(sliced)

    # "start at 4, stop at 2 at -1 increments" = print 4,3
        # sliced = x[4:2:-1]
        # print(sliced)

    # reverse a list (start at the start, stop at the end at -1 increments)
        # sliced = x[::-1]
        # print(sliced)

    # reverse list with "reverse()"
        # prime_nrs = [2,3,5,7]
        # prime_nrs.reverse()
        # print(prime_nrs)

        # list = [1,2,3,4,5]
        # list.reverse()
        # print(list)

# SETS (unordered unique collection of elements - "is it there or not there?", set notation: {x,x,x,x})
    # set = {4,32,2,2}
    # print(set)
    # s = {4,32,2,2}
    # s.add(5)
    # print(s)

    # check if in set (true/false)
    #     set = {4,32,2,2}
    #     print(2 in set)

# DICTIONARIES (smt in {}), a key tied to a value
    # x = {"key" : 4}
    # print("key" in x)

    # student = {"name" : "Mattias", "age" : 25, "courses" : ["Math", "CompSci"]}
    # print(student["name"])

# COMPREHENSIONS
    # x = [x for x in range(5)]
    # print(x)

# FUNCTION (block of code executed only when it's called, "invoking a code")

# first_name and second_name are parameters
    # def hello(first_name, second_name):
    #     print("Hello " + first_name, second_name)
    #     print("Have a nice day!")
    # # sending arguments to function
    # hello("Mattias", "Sylven")



























