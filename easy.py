"""# remove duplicates
def remove_duplicates(arr):
    k=[]
    for i in arr:
        if i not in k:
            k.append(i)
    return k
n=[1,2,2,3]
print(remove_duplicates(n))"""


"""#left_rotate
def left_rotate_by_one(arr):
    f=arr[0]
    for i in range (len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=f
    return arr
n=[1,2,3,4]
print(left_rotate_by_one(n))"""


"""#sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
        if i in arr:
            arr[i]>arr[i+1]
            return False
        return True
n=[2,3,1]
print(is_sorted(n))"""

"""#vowels
k=input("enter the string")
count=0
for i in k:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
print(count)"""

"""#even_odd
def count_even_odd(arr):
    even=0
    odd=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return(even,odd)
n=[1,2,3,4,5,6]
print(count_even_odd(n))"""


"""#unique
def unique_elements(arr1,arr2):
    a=[]
    for i in arr1:
        if i not in arr2:
            a.append(i)
    for i in arr2:
        if i not in arr1:
            a.append(i)
    return a
a=[1,2,3]
b=[3,4,5]
print(unique_elements(a,b))"""


"""#intersection
def intersection(arr1,arr2):
    a=[]
    for i in arr1:
        if i  in arr2 and i not in a:
            a.append(i)
    for i in arr2:
         if i in arr1 and i not in a:
            a.append(i)
    return a
a=[4,9,5]
b=[9,4,8]
print(intersection(a,b))"""

#minmax
def min_max(arr):
    a=arr[0]
    b=arr[0]
    for i in range(len(arr)):
        if arr[i]<a:
            a=arr[i]
        if arr[i]>b:
            b=arr[i]
    return a,b
n=[3,5,1,8,2]
print(min_max(n))
  
        
        
    




