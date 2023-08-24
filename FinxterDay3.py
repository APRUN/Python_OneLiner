# Revision:


    # g="ali"
    # if("a"in g):
    #     print("e")
    # else:
    #     print("1")

    # print(2+2 if 2>0  else 3+3)


# Lambda Function:
# map(function, iterables)


# txt=["Lambda func are anonymous functions","anynonymus functions do not have names","functions are objects in python"]

# mark=map(lambda s: (True,s) if "anonymus" in s else (False, s), txt)

# print(list(mark))



# Practice: 
emp={
    "Khalil":23,
    "Adnan":22,
    "Ali":2222,
    "Fatima":33   
 }

listy=map(lambda s: (("Hello") if s>1000 in s else ("Bye"))  , emp.items())
print(list(listy))



