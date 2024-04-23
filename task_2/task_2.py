# Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
import math 

def primeNumbers(a, b):

    if not isinstance(a, int) or not isinstance(b, int) :
        raise ValueError("Invalid input. Both values have to be 'int'")

    if a < b:
        numbers = range(a,b+1)
    else: 
        numbers = range(b,a+1)    
        
    primeNumbers = []

    for num in numbers:
        if num == 2 or num == 3:
            
            primeNumbers.append(num)

        if num >= 5:
            isPrime = True
            for i in range(2, int(math.sqrt(num))+1):
                
                if num % i == 0:
                    isPrime = False

            if isPrime:
                primeNumbers.append(num)            
                    

    return primeNumbers

if __name__ == '__main__':
    print(primeNumbers(20,10))                     