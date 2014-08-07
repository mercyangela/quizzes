"""Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example,
sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""

   
def calculate():
    numbers = list(())
    count = 0
    multiple = 1
    keep_going = "y"
    while keep_going == "y":
        data = input("Enter the number you want to add to the list: ")
        numbers.append(data)
        keep_going = input("If you want to add another number to the list enter y:")
    for y in list(numbers):
        count = count + int(y)
        multiple = multiple * int(y)
    print("The sum of all the members of the list is:", count)
    print("The multiplication of all the members of the list results in:", multiple)
calculate()


