# Selection sort in Python
arr = [6,2,4,1,7,8,9]
for x in range(len(arr)):
    index=x
    for y in range(len(arr)):
        if(arr[index]<arr[y]):
            temp=arr[index]
            arr[index]=arr[y]
            arr[y]=temp
print(arr)
