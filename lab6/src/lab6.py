def find_unreachable_cities(cities: list, storages: list, pipelines: list) -> list:
    graph = {node: [] for node in cities + storages}

    for u, v in pipelines:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

    result = []

    for storage in storages:
        visited = set()
        queue = [storage]
        visited.add(storage)

        while queue:
            current = queue.pop(0)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        unreachable = [city for city in cities if city not in visited]

        if unreachable:
            result.append([storage, unreachable])

    return result