# 13.1 查找
# 13.1.1 线性查找
def search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x: # item found, return the index value
            return i
    return -1 # loop finished, item was not in list

# 13.1.2 二分查找
def search(x, nums):
    low =0
    high = len(nums) -1
    while low <= high: # There is still a range to search
        mid = (low + high)//2 # position of middle item
        item = nums[mid]
        if x == item : # Found it! Return the index
            return mid
        elif x < item: # x is in lower half of range
            high = mid - 1 # move top marker down
        else: # x is in upper half
            low = mid + 1 # move bottom marker up
    return -1 # no range left to search, x is not there

# 13.1.3 比较算法

# 13.2 递归问题解决
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

fact(4)

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]

reverse("Hello")

def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
    return ans

anagrams("abc")

# 13.3 排序算法
# 13.3.1 选择排序
def selSort(nums):
    # sort nums into ascending order

    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]
        mp = bottom # bottom is smallest initially
        for i in range(bottom+1,n): # look at each position
            if nums[i] < nums[mp]: # this one is smaller
                mp = i # remember its index

    # swap smallest item to the bottom
    nums[bottom], nums[mp] = nums[mp], nums[bottom]

# 13.3.2 归并排序
def merge(lst1, lst2, lst3):
    # merge sorted lists lst1 and lst2 into lst3

    # these indexes keep track of current position in each list
    i1, i2, i3 = 0, 0, 0 # all start at the front
    n1, n2 = len(lst1), len(lst2)

    # Loop while both lst1 and lst2 have more items
    while i1< n1 and i2 < n2:
        if lst1[i1] < lst2[i2]: # top of lst1 is smaller
            lst3[i3] = lst1[i1] # copy it into current spot in lst3
            i1 = i1 + 1
        else: # top of lst2 is smaller
            lst3[i3] = lst2[i2] # copy it into current spot in lst3
            i2 = i2 + 1
        i3 = i3 + 1 # item added to lst3, update position

    # Here either lst1 or lst2 is done. One of the following loops will
    # execute to finish up the merge.

    # Copy remaining items (if any) from lst1
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from lst2
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1


def mergeSort(nums):
    # Put items of nums in ascending order
    n = len(nums)
    # Do nothing if nums contains 0 or 1 items
    if n > 1:
        # split into two sublists
        m= n //2
        nums1, nums2 = nums[:m], nums[m:]
        # recursively sort each piece
        mergeSort(nums1)
        mergeSort(nums2)
        # merge the sorted pieces back into original list
        merge(nums1, nums2, nums)


