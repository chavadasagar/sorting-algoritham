def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    else:
        mid = len(arr)//2 # it is used divide two part list

        left_arr = arr[mid:] # first 
        right_arr = arr[:mid] # last

        left_arr = merge_sort(left_arr) # recursion
        right_arr = merge_sort(right_arr) # recursion

        sorted_list = merge(left_arr,right_arr) # call merge function

        return sorted_list # it is a final result

def merge(left_arr,right_arr):
    s_list = [] # store sorted value one by one
    while(len(left_arr)!=0 and len(right_arr)!=0): # check if list is not empty then execute this 
        if(left_arr[0]<right_arr[0]):
            s_list.append(left_arr[0])
            left_arr.remove(left_arr[0])
        else:
            s_list.append(right_arr[0])
            right_arr.remove(right_arr[0])
        if(len(left_arr)!=0):
            s_list = s_list+left_arr
        if(len(right_arr)!=0):
            s_list = s_list+right_arr
        return s_list


arr = [6,5,4,3,2,1]

print(arr)
print(merge_sort(arr))
