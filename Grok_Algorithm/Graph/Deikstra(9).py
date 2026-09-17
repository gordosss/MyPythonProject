def dijkstra(graph, start, target):
    # 1. Инициализация таблиц
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parents = {}
    processed = set()

    # Поиск узла с наименьшей стоимостью среди ВСЕХ ещё не обработанных
    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_node = None
        for node, cost in costs.items():
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_node = node
        return lowest_node

    # 2. Основной цикл
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph.get(node, {})

        # Перебираем всех соседей текущего узла
        for neighbor, weight in neighbors.items():
            new_cost = cost + weight
            # Если новый путь дешевле ранее записанного — обновляем
            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.add(node)
        node = find_lowest_cost_node(costs)

    # 3. Восстановление пути от target назад к start
    path = []
    curr = target
    while curr in parents or curr == start:
        path.append(curr)
        if curr == start:
            break
        curr = parents.get(curr)

    final_path = path[::-1] if path and path[0] == start else []
      
    # Возвращаем кортеж: (минимальная_стоимость, список_маршрута)
    return costs.get(target, float('inf')), final_path


