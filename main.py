from random import randint
mas = [randint(0, 100) for a in range(10)]
n = len(mas)
step = n
print(mas)

while step > 1 or q:
    if step > 1:
        step -= 3
    q, i = False, 0
    while i + step < n:
        if mas[i] > mas[i + step]:
            mas[i], mas[i + step] = mas[i + step], mas[i]
            q = True
        i += step

print(mas)

'''
Алгоритм имеет сложность: 
в лучшем случае-O(n log n)
в худшем случае-O(n^2)

Идея алгоритма заключается в проходу по массиву с постепенно уменьшающимся шагом, то есть изначально мы берем большой 
шаг для сравнения 2ух элементов, а чем больше массив сортируется, тем меньше становится шаг
'''