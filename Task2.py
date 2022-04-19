#2.	Найти максимальное из пяти чисел

def Find_Max(m,n,x,y,z):
    max = m
    if n>max:
        max = n
    if x>max:
        max = x
    if y>max:
        max = y
    if z>max:
        max = z
    return max


a = int(input('Введите первое целое число ')) 
b = int(input('Введите второе целое число ')) 
с = int(input('Введите первое целое число ')) 
d = int(input('Введите второе целое число ')) 
e = int(input('Введите второе целое число ')) 

print('Максимум равен ', Find_Max(a,b,c,d,e))
