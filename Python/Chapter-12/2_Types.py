from typing import List, Union, Dict
#Types make the program easy to understand

a : int = 5
# When I write a. it will show me all the functions that can be used with int type

def add(a:int, b:int) -> int:
    return a+b
# Here when calling this function I can see what type of input is expected and what output I will get.

numbers : List[int] = [1, 2, 3, 4, 5] #Here we can use List from typing to show that this list is a list of integers.

dictionary: Dict[int, str] = {1:"Hello", 2:"World"}

score: Union[int, str] = "ABC123" #This indicates that the variable can hold multiple types