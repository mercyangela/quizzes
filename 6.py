"""Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example,
sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""

   
def sums():
    numbers = list(())
    count = 0
    keep_going = "y"
    while keep_going == "y":
        data = input("Enter the number you want to add to the list: ")
        numbers.append(data)
        keep_going = input("Do you want to enter another number? (enter y)")
    for y in list(numbers):
        count = count + int(y)
    print("The sum is:", count)
sums()

def multipy():
    
