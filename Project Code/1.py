nums = [4,5,5,9,9,2,2]
# nums.sort()
# print(nums)
# i=0
# for i in range(len(nums)-1):
#     if (nums[i]==nums[i+1]):
#         nums.remove(i+1)
#         i+=1
#         print(nums)
# else:
#     print(nums)

# x= str(nums)[1:-1]
# print(x)

# nums[:] = set(nums)
# print(nums)
# print(set(nums))

x= set(nums)
y= list(x)
z= sorted(y)
return(len(z))
