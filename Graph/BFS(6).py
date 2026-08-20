#Суть алгоритма:
#BFS ищет кратчайший путь по количеству шагов (например, связи 1-го уровня, 
#затем 2-го, затем 3-го). Он не пойдет дальше, пока не проверит всех ближайших соседей.

#Главная структура — Очередь (Queue):
#Работает по принципу FIFO (First In, First Out — кто первым встал, тот первым и вышел). 
#В Python для этого используют модуль deque из библиотеки collections.





from collections import deque

def bfs_shortest_path(graph, start, target):
    """
    Находит минимальное количество шагов от start до target.
    Возвращает число шагов (int) или -1, если путь не существует.
    """
    # 0. Проверка базового случая
    if start == target:
        return 0
    
    # 1. Очередь хранит кортежи: (текущий_узел, расстояние)
    queue = deque([(start, 0)])
    
    # 2. Множество запоминает ТОЛЬКО имена/узлы (без расстояний)
    visited = set([start]) #старт  помечется помещенным еще до входа в цикл
    
    while queue:
        # 3. Достаём узел из головы очереди (FIFO)
        current_node, distance = queue.popleft()
        
        # 4. Перебираем всех прямых соседей
        for neighbor in graph.get(current_node, []):
            
            # Если нашли цель — сразу возвращаем следующее расстояние
            if neighbor == target:
                return distance + 1
            
            # 5. Добавляем в очередь только новые узлы
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    # Путь не найден
    return -1
_____________________________________________________________________________________________



from collections import deque
def bfs_shortest_path(graph, start, target):
    if start == target:
        return 0
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        current_node, distance = queue.popleft()
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return distance + 1
            elif neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1)]
        return -1        


____________________________________________
#Базовый момент
from collections import deque
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)




from collections import deque


def bfs_shortest_path(graph, start, target):
    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()
        if current_node == path:
            return path
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
































































