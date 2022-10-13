from random import randint

N1 = int(input("Размерность первого массива: "))
N2 = int(input("Размерность второго массива: "))
array1 = [0] * N1
array2 = [0] * N2

for i in range(N1):
	array1[i] = randint(-5, 5)

for i in range(N2):
	array2[i] = randint(-5, 5)

print("Первый массив: ", array1)
print("Второй массив: ", array2)

resultArray = []

for i in array1:
    if i in array2:
      resultArray.append(i), array2.remove(i)

print(resultArray)