def get_kth_smallest_element(Matrix: list, k: int)-> int:

    last_row = len(Matrix) - 1
    last_col = len(Matrix[0]) - 1

    # Using Binary Search Approach
    low = Matrix[0][0]
    high = Matrix[last_row][last_col]


    while low < high:

        mid = (low+high)//2
        i = last_row
        j = 0
        count = 0
        
    # StairCase Search, starting from bottom right
        while i>=0 and j <= last_col:
            
            if Matrix[i][j] <= mid:
                count += i+1
                j += 1
            else:
                i -= 1   

        if count < k:
            low = mid+1
        else:
            high = mid

    return low

matrix =   [[1, 5, 9], 
          [10, 11, 13], 
          [12, 13, 15]]
k = 8
print(f"Input Matrix:-\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\nk = {k}th element\nOutput: "
      ,get_kth_smallest_element(matrix, k))