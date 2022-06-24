# -*- coding: utf-8 -*-

from rich import print
import time
import math
import random
from tabulate import tabulate

#print("[bold yellow]Программа для визначення найкращого алгоритму пошуку числа[/bold yellow]")

#print("[bold red]Алгоритми: [/bold red]")

def Linear_Search(lys, element):

    #print("[italic green]Linear Search (Лінійний пошук)[/italic green]")
    start_time = time.time()

    for i in range (len(lys)):
        if lys[i] == element:
            pass

    return time.time() - start_time


def Binary_Search(lys, element):

    #print("[italic green]Binary Search (Бінарний пошук)[/italic green]")
    start_time = time.time()

    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == element:
            index = mid
        else:
            if element<lys[mid]:
                last = mid -1
            else:
                first = mid +1

    return time.time() - start_time


def Jump_Search(lys, element):

    #print("[italic green]Jump Search (Стрибковий пошук)[/italic green]")
    start_time = time.time()

    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= element:
        right = min(length - 1, left + jump)
        if lys[left] <= element and lys[right] >= element:
            break
        left += jump;
    if left >= length or lys[left] > element:
        return time.time() - start_time
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= element:
        if lys[i] == element:
            return time.time() - start_time
        i += 1
    return time.time() - start_time

def Fibonacci_Search(lys, element):

    #print("[italic green]Fibonacci Search (Пошук Фібоначчі)[/italic green]")
    start_time = time.time()

    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < element):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > element):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return time.time() - start_time
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == element):
        return time.time() - start_time;
    
    return time.time() - start_time


def Interpolation_Search(lys, element):

    #print("[italic green]Interpolation Search (Інтерполяційний пошук)[/italic green]")
    start_time = time.time()

    low = 0
    high = (len(lys) - 1)
    while low <= high and element >= lys[low] and element <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( element - lys[low])))
        if lys[index] == element:
            return time.time() - start_time
        if lys[index] < element:
            low = index + 1;
        else:
            high = index - 1;
    
    return time.time() - start_time


def main():

    text1 = "Программа для визначення найкращого алгоритму пошуку числа"
    text2 = "Алгоритми: "
    text3 = "Linear Search (Лінійний пошук)"
    text4 = "Binary Search (Бінарний пошук)"
    text5 = "Jump Search (Стрибковий пошук)"
    text6 = "Fibonacci Search (Пошук Фібоначчі)"
    text7 = "Interpolation Search (Інтерполяційний пошук)"

    randomlist = []
    for i in range(0, 200 * 10**3):
        n = random.randint(0, 10 * 10**2)
        randomlist.append(n)
    element = random.randint(0, 10 * 10**2)

    a1 = Linear_Search(randomlist, element)
    a1 = float('{:.5f}'.format(a1))
    a1t = "Linear Search"
    a2 = Binary_Search(randomlist, element)
    a2 = float('{:.5f}'.format(a2))
    a2t = "Binary Search"
    a3 = Jump_Search(randomlist, element)
    a3 = float('{:.5f}'.format(a3))
    a3t = "Jump Search"
    a4 = Fibonacci_Search(randomlist, element)
    a4 = float('{:.5f}'.format(a4))
    a4t = "Fibonacci Search"
    a5 = Interpolation_Search(randomlist, element)
    a5 = float('{:.5f}'.format(a5))
    a5t = "Interpolation Search"

    list_times = [a1, a2, a3, a4, a5]
    list_names = [a1t, a2t, a3t, a4t, a5t]
    #print("[red](Тест проводиться на рандомних масивах довжиною 200 000 елементів)[red]")
    text8 = "(Тест проводиться на рандомних масивах довжиною 200 000 елементів)"
    top_time = []
    top_name = []

    for i in range(len(list_times)):
        index_min = min(range(len(list_times)), key=list_times.__getitem__)
        top_time.append(list_times[index_min])
        top_name.append(list_names[index_min])
        del list_times[index_min]
        del list_names[index_min]

    #print(top_name)
    #print(top_time)
    top_time1 = ["Час виконання: "] + top_time
    top_name1 = ["Алгоритм: "] + top_name

    data = [
        top_name1,
        top_time1
    ]

    #print("[bold blue]Таблиця лідерів[/bold blue]")
    text9 = "Таблиця лідерів"
    #print(tabulate(data, tablefmt="grid"))
    text10 = f"{top_name1}<br>{top_time1}"
    #print(f"[bold green]Найкращий алгоритм пошуку числа - {top_name[0]}[/bold green]")
    text11 = f"Найкращий алгоритм пошуку числа - {top_name[0]}"

    return f"{text1}<br>{text2}<br>{text3}<br>{text4}<br>{text5}<br>{text6}<br>{text7}<br>{text8}<br>{text9}<br>{text10}<br>{text11}"

#print(main())