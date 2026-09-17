#Бинарный поиск

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#Связные списки

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(head):
    curr = head
    while curr:
        # Логика обработки элемента (curr.val)
        curr = curr.next



#Рекурсия
def recursive_func(data):
    # 1. Базовый случай (выход из рекурсии)
    if not data:
        return 0
    # 2. Рекурсивный шаг
    return data[0] + recursive_func(data[1:])




#Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)



#Хеш таблицы
def two_sum(nums, target):
    seen = {}  # {значение: индекс}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []



#Поиск в ширину
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


#Поиск в глубину
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited                




#Алгоритм Дейкстры
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (расстояние, узел)
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
            
        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances




#Жадные алгоритмы
def greedy_set_cover(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states  # Пересечение
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered  # Вычитание
        final_stations.add(best_station)
    return final_stations




#Динамическое программирование
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]



#K-близжайшие соседи
import math

def euclidean_distance(pt1, pt2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(pt1, pt2)))

def get_k_neighbors(points, target, k):
    # points = [([x, y], label), ...]
    distances = [(euclidean_distance(pt[0], target), pt[1]) for pt in points]
    distances.sort(key=lambda x: x[0])
    return [label for _, label in distances[:k]]
