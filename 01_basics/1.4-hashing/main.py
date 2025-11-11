"""
Hashing is a fundamental technique used to uniquely identify and store data in a way that allows for extremely fast retrieval. The average time complexity for insertion, deletion, and search operations is O(1) (constant time).Its core idea is to use a special function, called a hash function, to convert an input (like a string, number, or object) into a fixed-size integer. This integer is then used as an index to store the data in an array called a hash table.
"""

"""
Given a array, and you are asking it multiple times like how many times some element apprears in the array 
Hashing. Collission. Division Method. (Refer: https://www.geeksforgeeks.org/dsa/hashing-data-structure/)
"""

"""
1. Given an array, we have found the number of occurrences of each element in the array.
"""
def count_occurances(array:list[int])->None:
    n = len(array)
    visited = [False] * n
    for i in range(0,n):
        if visited[i] == True:
            continue
        count = 1
        visited[i] = True

        for j in range(i+1,n):
            if array[i] == array[j]:
                count+=1
                visited[j] = True
        
        print(array[i], count)
numbers = [10, 20, 20, 10, 10, 20, 5, 20]
# count_occurances(numbers)


def print_min_max_freq(arr: list[int]):
    if not arr:
        return
    
    counts: dict[int, int] = {}

    for num in arr:
        counts[num] = counts.get(num,0) + 1
    
    min_freq = float('inf')
    max_freq = 0

    min_freq_num = None
    max_freq_num = None

    for num, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_num = num
        if freq < min_freq:
            min_freq = freq
            min_freq_num = num

    print(f"{max_freq_num} {min_freq_num}")   

array1 = [10, 5, 10, 15, 10, 5]
print_min_max_freq(array1)


"""
The same implementation but using counters from collections
"""

from collections import Counter

def print_min_max_freq_counter(arr: list[int]):
    # Handle the edge case of an empty list
    if not arr:
        return

    # 1. Counter() creates the frequency map (e.g., {10: 3, 5: 2, 15: 1})
    # 2. .most_common() converts it to a list of tuples,
    #    sorted from highest frequency to lowest.
    #    e.g., [(10, 3), (5, 2), (15, 1)]
    counts = Counter(arr).most_common()

    # The number with the max frequency is the first item
    # [0] gets the first tuple (10, 3), and [0] gets its number, 10
    max_freq_num = counts[0][0]

    # The number with the min frequency is the last item
    # [-1] gets the last tuple (15, 1), and [0] gets its number, 15
    min_freq_num = counts[-1][0]

    # 3. Print in the required format
    print(f"{max_freq_num} {min_freq_num}")
