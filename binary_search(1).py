#здесь задачи на бинарный поиск


def get_total_expenses(expenses):
    new_dict = {}
    for key in expenses:
        # 1. Вытаскиваем список чисел: expenses[key]
        # 2. Считаем его сумму: sum(...)
        new_dict[key] = sum(expenses[key])
    return new_dict


def get_cheap_items(prices, max_price):
    budget_100 = []
    for items in prices:
        if prices[items] <= 100:
            budget_100.append(items)
    return budget_100


def merge_dicts(dict1, dict2):
    dict3 = {}
    
    # 1. Заполняем dict3 данными из dict1
    for key, val in dict1.items():
        dict3[key] = val
        
    # 2. Добавляем данные из dict2
    for key, val in dict2.items():
        if key in dict3:
            dict3[key] += val  # Ключ совпал — складываем значения
        else:
            dict3[key] = val   # Ключа не было — просто записываем
            
    return dict3



def find_duplicates(numbers):
    counts = {}
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    duplicates = []
    for key, val in count.items():
        if val > 1:
            duplicates.append(key)



def reverese_list(lst):
    new_list = []
    i = len(lst) - 1
    while i >= 0:
        new_list.append(lst[i])
        i -= 1
    return new_list


def find_max_index(lst):
    max_number = 0
    max_index = 0
    i = len(lst) - 1
    while i >= 0:
        if lst[i] > max_number:
            max_number = lst[i]
            max_index = i
        i -= 1

    return max_index



def sum_pairs(lst):
    left = 0
    right = len(lst) - 1
    new_list = []
    while left < right:
        new_list.append(lst[left] + lst[right])
        left += 1
        right -= 1
    return new_list


def is_palindrome(s):
     left = 0 
     right = len(s) - 1
     while left < right:
         if s[left] != s[right]:
             return False
         else:
             left += 1
             right -= 1
    return True




def get_middle_element(lst):
    left = 0
    right = len(lst) - 1
    mid = (left + right)//2
    return lst[mid]

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid 
        elif lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
    return -1
             



def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) //2
        if lst[mid] == target:
            return mid 
        elif lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
    return -1



def search_insert(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) //2
        if lst[mid] == target:
            return mid     
        elif lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
    return left


def count_binary_steps(lst, target):
    left = 0
    right = len(lst) -1
    steps = 0  
    while left <= right:
        if lst[steps] == target:
            return steps
        elif lst[steps] != target:
            steps += 1
        else:
            return -1



