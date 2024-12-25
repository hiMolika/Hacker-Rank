# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def digonalDiff(arr):
    n = len(arr)
    left_dig_sum = 0
    right_dig_sum = 0

    for i in range(n):
        left_dig_sum += arr[i][i]
        right_dig_sum += arr[i][n-1-i]
    
    return abs(left_dig_sum-right_dig_sum)
arr = [[11, 2, 4], 
        [4, 5, 6], 
        [10, 8, -12]]

print(digonalDiff(arr))