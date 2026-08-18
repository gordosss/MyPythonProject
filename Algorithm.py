def two_sum(nums, target):
    seen = {}  # Словарь для хранения пар {число: индекс}    
    for i in range(len(nums)):
        needed = target - nums[i]        
        # Если нужное число уже встречалось ранее
        if needed in seen:
            return [seen[needed], i]  
        seen[nums[i]] = i



def first_uniq_char(s):
    counts = {}    
    # Шаг 1: Подсчитываем количество каждой буквы
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1            
    # Шаг 2: Ищем индекс первого уникального символа
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i  # Нашли первую уникальную букву — возвращаем индекс           
    return -1  # Уникальных букв нет



def zero(nums):
    last_none_zero = 0 
    for char in nums:
        if char != 0:
            nums[last_none_zero] = char
            last_none_zero += 1

            nums[last_none_zero] = 0
    return nums
            



def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        else:
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

    return low





    


















            