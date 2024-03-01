class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,k,j=0,0,len(nums)-1
        while(i<=j):
            if nums[i]==0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            else:
                i+=1
