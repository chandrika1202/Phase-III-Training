# Passing data from Parent function to child function
def findmin(i, n, nums,res):
    if n==i:
        print("min is :",res)
        return 
    if nums[i]<res:
        res=nums[i]
    findmin(i+1,n,nums,res)
nums = [12, 34, 56, 5, 7]
n = len(nums)
findmin(0, n, nums, nums[0])


# Passing data from child function to Parent function
def findmin1(i, n, nums):
    if n-1==i:
        return nums[i]
    min=findmin1(i+1,n,nums)
    if nums[i]<min:
        min=nums[i]
    return min
nums = [12, 34, 56, 5, 7]
n = len(nums)
print(findmin1(0, n, nums))
