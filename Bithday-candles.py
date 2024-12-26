'''
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .
'''

def tallest_candle(candles):
    tallest_height =0
    count = 0
    for height in candles:
        if height>tallest_height:
            tallest_height=height
            count = 1

        elif height == tallest_height:
            count +=1
    return count
candles =[3,2,1,3]
print(tallest_candle(candles))