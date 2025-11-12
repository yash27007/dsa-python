"""
Important sorting techniques such as selection sort, bubble sort and Insertion sort

"""

def selection_sort(array:list[int])->list[int]:
    for i in range(0,len(array)-1):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        if(min_index != i):
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp

    return array



def bubble_sort(array:list[int])->list[int]:
    n :int = len(array)
    swapped:bool = False
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j+1] = array[j]
                array[j] = temp
                swapped = True
        if not swapped:
            break
    return array




def insertion_sort(array:list[int])->list[int]:
    for i in range(0,len(array)):
        j = i
        while j > 0 and array[j-1] > array [j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j= j-1

    return array

print(insertion_sort([2,3,1,23,21,33,31,332,42]))
