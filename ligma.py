import random
import math
import math
import time
import sys
from heapq import heappush, heappop
issorted = True
def huskeysort(xs):
    global issorted
    if(issorted):
        random.shuffle(xs)
    introsort(hasher(xs),xs)

    x = sorted(hasher(xs))

    if(x != xs):
        return x
    return xs

def hasher(things):
    #4 is maxlength
    badhash=[]
    for thing in things:
        myval=0
        for char in thing:
            a = ord(char)
            myval+=a
        badhash.append(myval)
    return badhash

def introsort(alist,blist):
    maxdepth = (len(alist).bit_length() - 1)*2
    introsort_helper(alist,blist, 0, len(alist), maxdepth)
 
def introsort_helper(alist,blist, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heapsort(alist,blist, start, end)
    else:
        p = partition(alist,blist, start, end)
        introsort_helper(alist,blist, start, p + 1, maxdepth - 1)
        introsort_helper(alist,blist, p + 1, end, maxdepth - 1)
 
def partition(alist,blist, start, end):
    pivot = alist[start]
    i = start - 1
    j = end
 
    while True:
        i = i + 1
        while alist[i] < pivot:
            i = i + 1
        j = j - 1
        while alist[j] > pivot:
            j = j - 1
 
        if i >= j:
            return j
 
        swap(alist,blist, i, j)
 
def swap(alist,blist, i, j):
    alist[i], alist[j] = alist[j], alist[i]
    blist[i],blist[j]=blist[j],blist[i]
 
def heapsort(alist,blist, start, end):
    build_max_heap(alist,blist, start, end)
    for i in range(end - 1, start, -1):
        swap(alist,blist, start, i)
        max_heapify(alist,blist, index=0, start=start, end=i)
 
def build_max_heap(alist,blist, start, end):
    def parent(i):
        return (i - 1)//2
    length = end - start
    index = parent(length - 1)
    while index >= 0:
        max_heapify(alist,blist, index, start, end)
        index = index - 1
 
def max_heapify(alist,blist, index, start, end):
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
 
    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and alist[start + l] > alist[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[start + r] > alist[start + largest]):
        largest = r
    if largest != index:
        swap(alist,blist, start + largest, start + index)
        max_heapify(alist,blist, largest, start, end)

# Python3 program to perform basic timSort
# Got TimSort From GeeksForGeeks to Compare
MIN_MERGE = 32
  
def calcMinRun(n): 
    """Returns the minimum length of a  
    run from 23 - 64 so that 
    the len(array)/minrun is less than or  
    equal to a power of 2. 
  
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,  
    ..., 127=>64, 128=>32, ... 
    """
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 
  
  
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1
  
  
# Merge function merges the sorted runs 
def merge(arr, l, m, r): 
      
    # original array is broken in two parts 
    # left and right array 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[l + i]) 
    for i in range(0, len2): 
        right.append(arr[m + 1 + i]) 
  
    i, j, k = 0, 0, l 
      
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
  
        else: 
            arr[k] = right[j] 
            j += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1
  
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
      
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 
  
    # Start merging from size RUN (or 32). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
          
        # Pick starting point of left sub array. We 
        # are going to merge arr[left..left+size-1] 
        # and arr[left+size, left+2*size-1] 
        # After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            # arr[mid+1....right] 
            merge(arr, left, mid, right) 
  
        size = 2 * size 
  

if __name__ == "__main__":
    
    infile = open("test.txt").read().split("\n")
    mylist = infile.copy()
    start = time.time()
    huskeysort(infile)
    print("Huskysort time: ",time.time()-start)
    start = time.time()
    timSort(hasher(mylist))
    print("Timsort time: ",time.time()-start)
    
    
