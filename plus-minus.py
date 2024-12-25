# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

def plusminus(arr):

    n = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in arr :
        if num>0:
            positive_count += 1
        elif num<0:
            negative_count += 1
        else:
            zero_count += 1
    
    positive_ratio = positive_count/n
    negative_ratio = negative_count/n
    zero_ratio = zero_count/n

    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

arr = list(map(int,input().split()))
print(plusminus(arr))
