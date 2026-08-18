def get_user_role(users, username):
    if username in users:
        return users[username]
    else:
        return 'Guest'
#вопрос, что за метод get


def filter_scores(scores, min_score):
    result = {}
    #что за for key, val in scores.items()
    for key, val in scores.items():
        if val >= min_score:
            result[key] = val
    return result



def count_letters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def most_frequent_word(words):
    counts = {}
    for char in words:
        if char in counts:
            words[char] += 1
        elif char not in words:
            words[char] = 1
    max_word = ''
    max_count = 0
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word, max_count



def group_by_length(words):
    counts = {}
    for word in words:
        length = len(word)  # Считаем длину текущего слова
        
        if length not in counts:
            counts[length] = []  # Создаём пустой СПИСОК для такой длины
            
        counts[length].append(word)  # Добавляем слово в список
        
    return counts


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_1 = {}
    s2_2 = {}
    for char in s1:
        if char not in s1_1:
            s1_1[char] = 1
        elif char in s1_1:
            s1_1[char] += 1
    for char in s2:
        if char not in s2_2:
            s2_2[char] = 1
        elif char in s2_2:
            s2_2 += 1
    return s1_1 == s2_2

            

def group_by_parity(numbers):
    result = {'even':[], 'odd':[]}
    #even - четные
    #odd - нечетные
    for num in numbers:
        if num % 2 == 0:
            result['even'].append(num)
        else:
            result['odd'].append(num)
    return result


def get_freq(lst):
    counts = dict()  # Можно писать dict() или {} — оба варианта верны!
    for item in lst:  # Добавили цикл по списку
        if item in counts: 
            counts[item] += 1
        else:
            counts[item] = 1
    return counts






