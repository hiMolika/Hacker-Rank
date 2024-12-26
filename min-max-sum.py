'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

'''

def min_max_sum(arr):
    # calculate the total sum
    total = 0
    for num in arr:
        total += num
    
    # find max and min value
    min = arr[0]
    max = arr[0]
    for num in arr:
        if num<min:
            min = num
            print("min:",min)
        if num>max:
            max = num
            print("max:",max)
    min_sum = total - max
    max_sum = total - min

    print(min_sum,max_sum)

arr = [1,3,5,7,9]
print(min_max_sum(arr))