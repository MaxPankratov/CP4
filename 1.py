N = int(input("Размерность массива: "))
array = [0] * N

for i in range(N): 
	print("Элемент", i+1, "= ", end="") 
	array[i] = float(input()) 

print("Входной массив: ", array)

maxElementIndex = 0

for i in range(1, N):
    if (array[i] >= array[maxElementIndex]):
        maxElementIndex = i
		  
for i in range (maxElementIndex + 1, N):
    array[i] = 0

print("Результат: ", array)