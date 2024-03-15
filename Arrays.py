#!/usr/bin/env python
# coding: utf-8

# In[1]:
a = ["BMW","AUDI","MARUTI","TATA","TESLA"]


# In[2]:
## Using indexing we can print any value of array
print(a[2])
print(a[-1])


# In[3]:
## using loop in array
for x in a:
    print(x)


# In[4]:
## calculating the amount of value present
len(a)


# ## ARRAY METHODS

# In[5]:
# append()
a.append("SKODA")


# In[6]:
a


# In[7]:
# copy()
b = a.copy()


# In[8]:
b


# In[9]:
# count()
a.count("AUDI")


# In[10]:
# extend()
a.extend(["MAHINDRA","FORD"])


# In[11]:
a


# In[14]:
b.extend([1,2,3,4])


# In[15]:
b


# In[12]:
# index()
a.index("TATA")

Note: The index() method only returns the first occurrence of the value.

    
# In[16]:
# insert()
a.insert(5,"KIA")


# In[17]:
a
Note: insert element can be of any type (string, number, object etc.)


# In[18]:
# pop()
a.pop(4)


# In[19]:
a.pop()
Note: By default pop removes last element of the array.


# In[20]:
# reverse()
a.reverse()


# In[21]:
a


# In[22]:
# clear()
b.clear()


# In[23]:
b


# In[24]:
#sort
a.sort()


# In[25]:
a

Note: sort has two parameter
    
    1. reverse.
    2. key


# In[26]:
a.sort(reverse=True)


# In[27]:
a


# In[32]:
a.sort(reverse=0)  # 0 = False, 1 = True


# In[33]:
a


# In[38]:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)
a.sort(key=myFunc)


# In[39]:
a


# In[40]:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)

a.sort(reverse=1,key=myFunc)


# In[41]:
a


# ## QUESTIONS
1. Find the Missing Number: 
   Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# In[7]:
def missing_number(arr):
    missed_number = []
    for i in range(n):
        if i not in arr:
            missed_number.append(i)
    return missed_number


# In[8]:
n = 7
arr_1 = [0,1,2,3,5,7]
missing_number(arr_1)

NOTE: for constant n, the time complexity of code is O(n)

2. Find the Duplicate Number:
   Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n], find the duplicate one.
# In[22]:
def duplicate_number(arr):
    duplicate_array = []
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] not in duplicate_array:
            duplicate_array.append(arr[i])
    return duplicate_array


# In[23]:
n = 8
arr_2 = [1,3,5,8,2,6,7,4,3]
duplicate_number(arr_2)

NOTE: for constant n,
    - time taken by sort() is O(n logn)
    - time taken by for loop is O(n)
    Total time complexity of code is O(n logn).
                   
alternative approach ( USING ABS() )
-- abs() , it is the positve distance between 0 and number(x)


# In[30]:
print(abs(3))
print(abs(-7))


# In[29]:
def duplicate_number(arr):
    duplicate_array = []

    for num in arr:
        index = abs(num) - 1
        if arr[index] < 0 and num not in duplicate_array:
            duplicate_array.append(num)
        else:
            arr[index] = -arr[index]

    return duplicate_array

- time taken by for loop is O(n)
- time taken by abs, if condition is O(1)
Total time complexity is O(n).

3. Largest Sum Contiguous Subarray (Kadane's Algorithm): 
   Find the contiguous subarray within an array (containing at least one number) that has the largest sum.
# In[8]:
def max_sum_subarr(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    curr_point = 0
    start_point = 0
    end_point = 0
    
    for i in range(1,len(arr)):
        if arr[i] > curr_sum + arr[i] :
            curr_sum = arr[i]
            curr_point = i
        else:
            curr_sum += arr[i]
            
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = curr_point
            end = i
    return arr[start:end+1],max_sum


# In[9]:
arr_3 = [-2, 1, -3, 4, 7, -1, 2, 1, -5, 4]
max_sum_subarr(arr_3)

- time taken by for loop is O(n)
- time taken by if condition and assign is O(1)
Total time complexity is O(n)

4. Rotate Array: 
Rotate an array of n elements to the right by k steps.
# In[3]:
def rotate_byK(arr,k):
    if arr is None:
        return arr
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


# In[4]:
arr_4 = [1,3,5,7,9]
rotate_byK(arr_4,2)

- time taken for initializing is O(1)
- taken taken for concatenating is O(n)
Total time complexity is O(n)

5.Merge Sorted Arrays: 
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# In[6]:
def sorted_arrs(arr1,arr2):
    return sorted(arr1 + arr2)


# In[19]:
num1 = [1, 3, 5, 7]
num2 = [2, 4, 6, 8]
sorted_arrs(num1,num2)

- time taken by sorted() is O(n log(n))
Total time complexity is O(n log(n))


# In[10]:
## alternative approach


# In[18]:
def sorted_arrs_2(arr1,arr2):
    i = len(arr1) - 1            # indexing for arr1
    j = len(arr2) - 1            # indexing for arr2
    k = len(arr1) + len(arr2) - 1
    arr1 = arr1 + [0 for i in range(j+1)]
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i-=1
        else:
            arr1[k] = arr2[j]
            j-=1
        k-=1
    while j >=0:
        arr1[k] = arr2[j]
        j-=1
        k-=1
    return arr1


# In[19]:
num1 = [1, 3, 5, 7]
num2 = [2, 4, 8, 10]
sorted_arrs_2(num1,num2)

- time taken to append 0 in arr1 is O(len(num2)) ,since both arrays are of size "n" , O(n)
- time taken to iterate both array and merging them is O(n+n)
- time taken to copying any left element in arr2 is O(n)
Total time complexity is O(n)

6. Find Peak Element: 
A peak element in an array is an element that is greater than its neighbors. Find the peak element and return its index.
# In[31]:


def peak_element(arr):
    n = len(arr)
    
    if n == 1 or arr[0] >= arr[1]:
        print(0)
    
    if arr[n-1] >= arr[n-2]:
        print(n-1)
    
    for k in range(1,n-1):
        if arr[k-1] <= arr[k] >= arr[k+1]:
            print(k)
    return


# In[32]:
arr_6 = [5,4,3,2,6]
peak_element(arr_6)

- time taken to check first and last element is O(1)
- time taken in loop to find peak element is O(n-2)
- time taken to print the element is O(1)
Total time complexity is O(n)


# In[34]:
## Alternative appraoch using binary search


# In[12]:
def peak_element_2(arr):
    n = len(arr)
    i = 0
    j = n - 1
    
    while i <= j:
        mid = (i + j) // 2
        
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            print(mid)
        
        if mid > 0 and arr[mid - 1] > arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return


# In[13]:
arr_6 = [5,4,3,2,6]
peak_element_2(arr_6)

- time taken for mid term of each element is O(n/2)
- time taken for initailizing `is O(1)
Total time complexity is O(logn)

7. Search in Rotated Sorted Array: 
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given a target value, return the index if the target is found, or -1 if it is not found
# In[20]:
def search_element(arr,k):
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


# In[21]:
arr_7 = [3,4,5,1,2]
search_element(arr_7,2)

- time taken by loop is O(n)
Total time complexity is O(n)

# In[22]:
## alternative approach using binary search|


# In[11]:
def search_element_2(arr,k):
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = (i+j) //2
        
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            m = mid
            break
        if mid > 0 and arr[mid - 1] > arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    
    i = 0
    j = m
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            i = mid + 1
        else:
            j = mid - 1

    i = m
    j = len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            i = mid + 1
        else:
            j = mid - 1

    return -1


# In[12]:
arr_7 = [3,4,5,1,2]
search_element_2(arr_7,2)

- Time taken to find the peak element is O(logn)
- Time taken to find the required element in the arr is O(logn)
Total time complexity is O(logn)

8. Maximum Product Subarray: 
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product.
# In[17]:
def max_product_arr(arr):
    if not arr:
        return None, 0
    
    max_prod = arr[0]
    curr_prod = arr[0]
    max_start = max_end = curr_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > curr_prod * arr[i]:
            curr_prod = arr[i]
            curr_start = i
        else:
            curr_prod *= arr[i]
        
        if curr_prod > max_prod:
            max_prod = curr_prod
            max_start = curr_start
            max_end = i
    
    return arr[max_start:max_end + 1], max_prod


# In[18]:
arr_8 = [6, -3, -10, 0, 2]
max_product_arr(arr_8)

- Time taken in for traversing the element is O(n)
- Time taken in conditional and assigning is O(1)
Total time complexity is O(n)

9. Two Sum: 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# In[53]:
def target_sum(arr, target):
    dict = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in dict:
            return dict[complement],i
        dict[num] = i
    return


# In[54]:
arr_9 = [1,3,9,4]
target_sum(arr_9,7)

- Time taken for iterating is O(n)
- Time taken to find index in dictionary is O(1)
Total time complexity is O(n)

10. Move Zeroes: 
Given an array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# In[57]:
def zeroes_moves_arr(arr):
    n = len(arr)
    c = 0
    for i in range(n):
        if arr[i] != 0 :
            arr[c] = arr[i]
            c +=1
    
    while c < n:
        arr[c] = 0
        c+=1
    return arr


# In[58]:
arr_10 = [1,0,4,0]
zeroes_moves_arr(arr_10)

- Time taken in for loop is O(n)
- Time taken in conditional or assign is O(1)
Total time complexity is O(n)
