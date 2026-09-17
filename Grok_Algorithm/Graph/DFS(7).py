# Граф папок: имя папки -> список вложенных папок
folders = {
    "C:": ["Documents", "Downloads"],
    "Documents": ["Projects", "Photos"],
    "Projects": [],
    "Photos": [],
    "Downloads": []
}

def dfs(graph, current_folder, visited=None):
    if visited is None:
        visited = set()

    print(f"Открыли папку: {current_folder}")
    visited.add(current_folder)

    # Заглядываем внутрь текущей папки
    for subfolder in graph[current_folder]:
        if subfolder not in visited:
            dfs(graph, subfolder, visited)  # Шаг вглубь: заходим во вложенную папку

# Запуск
dfs(folders, "C:")

_______________________________________________________________
#Базовый момент

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)