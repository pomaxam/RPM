if __name__ == '__main__':
    import math
    print("Введите переменные")
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    dis = b ** 2 - 4 * a * c
    print("b^2-4ac = ", dis)
    if dis > 0:
        x1 = (-b - math.sqrt(dis)) / (2 * a)
        x2 = (-b + math.sqrt(dis)) / (2 * a)
        print("x1 = ", x1,"x2 = ",x2)
    elif dis == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        print("Корней нет")
