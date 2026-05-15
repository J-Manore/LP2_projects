from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# DFS
dfs_result = []

def dfs(node, visited):
    
    if node not in visited:
        print(f"Visiting: {node}")
        visited.add(node)
        dfs_result.append(node)
        for neighbor in graph[node]:
            print(f"  {node} -> {neighbor}")
            dfs(neighbor, visited)

# BFS
def bfs(start):

    visited = set()
    queue = deque([start])
    bfs_result = []
    while queue:
        print("Queue:", list(queue))
        node = queue.popleft()
        if node not in visited:
            print(f"Visiting: {node}")
            visited.add(node)
            bfs_result.append(node)
            for neighbor in graph[node]:
                print(f"  Adding {neighbor} to queue")
            queue.extend(graph[node])
    return bfs_result


print("DFS:")
dfs('A', set())

print("\nDFS Sequence:")
print(" -> ".join(dfs_result))

print("\nBFS:")
bfs_result = bfs('A')

print("\nBFS Sequence:")
print(" -> ".join(bfs_result))