# O(n) time, quick selection
def findKthLargest(nums, k):
    # convert the kth largest to smallest
    return findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(nums, k):
    # choose the right-most element as pivot   
    def partition(l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
    if nums:
        pos = partition(0, len(nums)-1)
        if k > pos+1:
            return findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
