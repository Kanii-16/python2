"""# average marks
students = [("A",85),("B",40),("C",72 ),("D",30)]

passed_students=[]
total_marks=0

top_name = students[0][0]
top_marks = students[0][1]

for name ,marks in students:
    if marks >=50:
        passed_students.append(name)
        
    total_marks= total_marks+marks
    if marks > top_marks:
        top_marks=marks
        top_name=name
        
average = total_marks/len(students)

print("passed students:",passed_students)
print("average marks:",average)
print("topper:",top_name,top_marks)"""

#rotate array
def rotate_to_sorted(arr):
 n=len(arr)
 index = 0

 for i in range(n-1):
     if arr[i] > arr[i+1]:
        index = i+1
        break
 return arr[index:]+arr[:index]
arr=[4,5,6,1,2,3]
print(rotate_to_sorted(arr))