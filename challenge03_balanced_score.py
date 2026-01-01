def calculate_median(arr1: list, arr2: list)-> float:

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    n = len_arr1 + len_arr2

    middle_val = n//2

    ptr1 = 0
    ptr2 = 0
    current_val = None
    previous_val = None

    for i in range(middle_val+1):
        previous_val = current_val

        if ptr1 < len_arr1 and (ptr2>= len_arr2 or arr1[ptr1]<arr2[ptr2]):
            current_val = arr1[ptr1]
            ptr1 += 1
        else:
            current_val = arr2[ptr2]
            ptr2 +=1
    
    # print(current_val)
    # print(previous_val)

    if n%2 != 0:
        return float(current_val)
    else:
        return (current_val+previous_val)/2

arr1 = [1,2]
arr2 = [3,4,5]
print(calculate_median(arr1, arr2))
