array = [int(i) for i in input("Введите элементы массива, разделяя их пробелом: ").split()] 
Delta = int(input("Введите значение Delta: "))

minElement = array[0]

for i in range(len(array)):
    if (array[i] <= minElement):
        minElement = array[i]
		  
counter = 0

for i in array:
    if i == Delta + minElement:
        counter += 1

print(counter)