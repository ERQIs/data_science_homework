from time import time
from random import randint

def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n-1):
    for j in range(n-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
  return arr

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  
  left_arr = merge_sort(left_arr)
  right_arr = merge_sort(right_arr)
  
  return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
  merged_arr = []
  left_idx = 0
  right_idx = 0
  lar = len(left_arr)
  rar = len(right_arr)
  while left_idx < lar and right_idx < rar:
    if left_arr[left_idx] < right_arr[right_idx]:
      merged_arr.append(left_arr[left_idx])
      left_idx += 1
    else:
      merged_arr.append(right_arr[right_idx])
      right_idx += 1
  
  while left_idx < lar:
    merged_arr.append(left_arr[left_idx])
    left_idx += 1
    
  while right_idx < rar:
    merged_arr.append(right_arr[right_idx])
    right_idx += 1
  
  return merged_arr

print("lenth of array to sort: ")
n = int(input())

print("generating random array...")
a1 = []
for i in range(n):
    a1.append(randint(1, 100000000))
a2 = a1[:]

print("testing bubble sort...")
start_time = time()
bubble_sort(a1)
end_time = time()
print("bubble sort time used: {:.5f}s".format(end_time - start_time))

print("testing merge sort...")
start_time = time()
merge_sort(a2)
end_time = time()
print("merge sort time used: {:.5f}s".format(end_time - start_time))

