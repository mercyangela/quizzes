def is_member():
    value = input("Enter the value you want to crosscheck in the list.")
    if value is not '':
        List = input('Enter items that you will be comparing this with.')
    else:
        print("No value was entered,please insert value to compare with.")
    for i in range(len(List)):
        if value == List[i]:
            print('The given value is present in the given string.')
        else:
            print('The given value is NOT present in the given string.')
is_member()
