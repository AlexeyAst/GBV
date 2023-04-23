
def printarr(textarr, lenarr, list):
    print(textarr)
    typearr = "["
    for cours in range(len(list)):
        if cours == lenarr-1: symb = "]"
        else:
            symb = ", "
        typearr = typearr + list[cours] + symb
    print(typearr)    


listitog = []

print("Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам.")
print("Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.")
print()
if int(input('1 - Вы хотите самостоятельно ввести элементы массива, 2 - Хотите воспользоваться готовым примером ')) == 1:
    lenarr = int(input("Введите размер массива: "))
    listish = []
    for i in range(lenarr):
        listish.append(input("Введите следующий элемент "))
else:
    lenarr = 7
    listish = ["тип", "фйпып", "ваыв", "ьлопрываолк", "да", "ёж", "фываопрыв"]

for cours in range(lenarr):
    if len(listish[cours])<=3: listitog.append(listish[cours])

printarr("Исходный массив:", lenarr, listish)
printarr("Итоговый массив:", len(listitog), listitog)





 