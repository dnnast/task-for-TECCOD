# Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
import math

def sortAscending(arr):
    for i in range(len(arr)):

        for j in range(len(arr)- i-1):

            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr  

def sortDescending(arr):
    arr = sortAscending(arr)

    for i in range(math.ceil(len(arr)/2)):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]

    return arr 

def sort(arr):
    if(len(arr) < 2):
        return arr

    return sortDescending(sortAscending(arr))


def printLinesLen(arr):
    for line in arr:
        print('Length: {}\nLine: {}\n'.format(len(line), line))       


if __name__ == '__main__':
    # lines = ['loop', 'to', 'compare', 'array', 'elements']
    lines = [
        'Create a list L with three string elements containing newline characters.',
        'Open a file named myfile.txt in write mode and assign it to the variable file1.',
        'Write the contents of the list L to the file using the writelines() method of the file object file1.',
        'Close the file object file1 using the close() method.',
        'Open the file named myfile.txt in read mode and assign it to the variable file1.',
        'Initialize a variable count to 0.',
        'Start an infinite loop.'
    ]

    linesSorted = sort(lines)      
    printLinesLen(linesSorted)