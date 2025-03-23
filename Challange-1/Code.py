def max_profit(nums):
    min_price= float('inf')
    max_profit=0
    for i in range(1,len(nums)):
        if nums[i]<min_price:
            min_price=nums[i]
        else:
            profit=nums[i]-min_price
            max_profit=max(max_profit,profit)
    return max_profit
a=[5,7,1,5,3,6]
b=[4,10,9,8,6]
print("For array:",a,"the max profit is:",max_profit(a))
print("For array:",b,"the max profit is:",max_profit(b))