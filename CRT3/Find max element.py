# Passing data from Parent function to child function
def findmax(i, n, nums,res):
    if n==i:
        print("max is :",res)
        return 
    if nums[i]>res:
        res=nums[i]
    findmax(i+1,n,nums,res)
nums = [12, 34, 56, 5, 7]
n = len(nums)
findmax(0, n, nums)

# Passing data from child function to Parent function
def findmax1(i, n, nums):
    if n-1==i:
        return nums[i]
    max=findmax1(i+1,n,nums)
    if nums[i]>max:
        max=nums[i]
    return max
nums = [12, 34, 56, 5, 7]
n = len(nums)
print(findmax1(0, n, nums))


