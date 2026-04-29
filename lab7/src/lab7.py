import os

INF = 10**9

def build_graph(lines):
    graph = {}
    source = "SUPER_SOURCE"
    sink = "SUPER_SINK"

    def add_edge(u, v, cap):
        if u not in graph: graph[u] = {}
        if v not in graph: graph[v] = {}
        graph[u][v] = graph[u].get(v, 0) + cap
        if u not in graph[v]: graph[v][u] = 0

    farms = [f.strip() for f in lines[0].split(",")]
    for farm in farms:
        add_edge(source, farm, INF)

    stores = [s.strip() for s in lines[1].split(",")]
    for store in stores:
        add_edge(store, sink, INF)

    for line in lines[2:]:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == 3:
            u, v, cap = parts[0], parts[1], int(parts[2])
            add_edge(u, v, cap)

    return graph, source, sink

def bfs(graph, s, t, parent):
    visited = {s}
    queue = [s]
    
    i = 0
    while i < len(queue):
        u = queue[i]
        i += 1
        for v, cap in graph[u].items():
            if v not in visited and cap > 0:
                parent[v] = u
                visited.add(v)
                if v == t:
                    return True
                queue.append(v)
    return False

def calculate_max_flow(filepath):
    if not os.path.exists(filepath):
        print(f"Помилка: Файл за шляхом {filepath} не знайдено!")
        return 0

    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) < 3: return 0

    graph, source, sink = build_graph(lines)
    max_flow = 0
    parent = {}

    while bfs(graph, source, sink, parent):
        path_flow = INF
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, graph[prev][curr])
            curr = prev
        
        max_flow += path_flow
        
        curr = sink
        while curr != source:
            prev = parent[curr]
            graph[prev][curr] -= path_flow
            graph[curr][prev] += path_flow
            curr = prev
            
    return max_flow

if __name__ == "__main__":
    path = os.path.join("src", "roads.csv")
    result = calculate_max_flow(path)
    print(f"Максимальна кількість машин: {result}")