arr = [3,2,1] # before sort

temp = 0

for x in range(len(arr)):

    for y in range(len(arr)):

        if(arr[x]<arr[y]):
            temp = arr[x]
            arr[x]=arr[y]
            arr[y]=temp




print(arr) #after sort
