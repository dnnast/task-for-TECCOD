import time

# Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def uniqueNumbers(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers

    def heapify(arr, N, i):
        max = i
        leftChild = 2*i + 1 
        rightChild = 2*i + 2

        if leftChild < N and arr[i] < arr[leftChild]:
            max = leftChild

        if rightChild < N and arr[max] < arr[rightChild]:
            max = rightChild

        if max != i:
            arr[i], arr[max]  = arr[max], arr[i] 
            heapify(arr, N, max)           


    def heapSort(arr):
        N = len(arr)

        for i in range(N//2 - 1, -1, -1):
            heapify(arr, N, i)

        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        
    # sort the numbers
    heapSort(numbers)

    # remove duplicates
    i = 0
    while i < len(numbers)-1:
        if numbers[i] == numbers[i+1]:
            numbers.pop(i+1)
        else:
            i+=1

    return numbers        
  

if __name__ == '__main__':
    numbers = [1,2,13,4,5,0,2,2,5,5,46,3,4,6,9]


    print("List: ", (numbers), "\n")

    print("Unique Numbers:")

    start_time = time.time()
    print(uniqueNumbers(numbers))
    end_time = time.time()
    print("Execution time: ", end_time-start_time) 
