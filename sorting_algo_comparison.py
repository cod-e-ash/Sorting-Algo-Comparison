# ***************************************
#  Sorting Fucntions created by Ashish
# ***************************************

# ----------------------------------------
#  Merge Sort
# ----------------------------------------
import numpy as np
import time

def merge(l,r):
    l_range = len(l)
    r_range = len(r)
    
    i = 0
    j = 0
    outarr = []

    while j < r_range and i < l_range:
        if l[i]<r[j]:
            outarr.append(l[i])
            i+=1
        else:
            outarr.append(r[j])
            j+=1
    while i < l_range:
        outarr.append(l[i])
        i+=1
    while j < r_range:
        outarr.append(r[j])
        j+=1
    
    return outarr

def mergesort(arr):
    # l = []
    # r = []
    if len(arr) > 2:
        m = int(len(arr)/2)
        l = mergesort(arr[:m])
        r = mergesort(arr[m:])
    else:
        m = 1
        l = arr[:m]
        r = arr[m:]
    return merge(l,r)

# ----------------------------------------
#  Bubble Sort
# ----------------------------------------
def bubsort(x):
    for j in range(len(x)-1):
        for i in range(len(x) - j - 1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x



# ----------------------------------------
#  Quick Sort
# ----------------------------------------

def quicksort(x,start=0,end=None):
    if end == None:
        end = len(x)-1
    def _quicksort(x,start=0,end=None):
        pivpos = end
        i = start
        while i < pivpos:
            if x[pivpos]<x[i]:
                x[i],x[pivpos],x[pivpos-1]=x[pivpos-1],x[i],x[pivpos]
                pivpos -= 1
                i-=1
            i+=1
        if pivpos-1 > start:
            _quicksort(x,start,pivpos-1)
        if pivpos+1 < end:
            _quicksort(x,pivpos+1,end)
    _quicksort(x,start,end)
    return x

# ----------------------------------------
#  Main Function
# ----------------------------------------

def main():
    sample_size = 10000
    myarr = list(np.random.random_integers(1,100000,sample_size))
    myarrc = myarr.copy()

    start_time = time.time()
    mergesort(myarr)
    #print(mergesort(myarr))
    print("Merge sort takes %s seconds for %d sample" % (time.time() - start_time, sample_size))

    start_time = time.time()
    bubsort(myarr)
    #print(bubsort(myarr))
    print("Bubble sort takes %s seconds for %d sample" % (time.time() - start_time, sample_size))

    start_time = time.time()
    quicksort(myarrc)
    #print(quicksort(myarrc))
    print("Quick sort takes %s seconds for %d sample" % (time.time() - start_time, sample_size))

if __name__ == "__main__":
    main()

