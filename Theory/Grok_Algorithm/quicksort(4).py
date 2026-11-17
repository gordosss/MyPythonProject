def sum_dc(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_dc(lst[1:])
    

def quicksort(lst):
    if len(lst) < 2:
        return lst
    
    pivot = lst[0]
    # Используем одинаковые переменные i и в цикле, и в условии:
    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def filter_numbers(numbers):
    bigger_five = [x for x in numbers if x > 5]
    return bigger_five



def max_dc(lst):
    if len(lst) == 1:
        return lst[0]
    sub_max = max_dc(lst[1:])#я не понял как это должно сработать
    if lst[0] > sub_max:
        return lst[0]
    else:
        return sub_max
    
