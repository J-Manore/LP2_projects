import heapq

def heuristic(word, goal):
    count = 0
    for i in range(len(word)):
        if word[i] != goal[i]:
            count += 1
    return count


def get_neighbors(word, words):
    neighbors = []
    for w in words:
        diff = 0
        for i in range(len(word)):
            if word[i] != w[i]:
                diff += 1
        if diff == 1:
            neighbors.append(w)
    return neighbors

def astar(start, goal, words):
    pq = [(0, start)]
    g = {start: 0}
    parent = {start: None}
    while pq:
        f, word = heapq.heappop(pq)
        print(f"\nVisiting: {word}")
        if word == goal:
            print("\nGoal Reached!")
            path = []
            while word:
                path.append(word)
                word = parent[word]
            path.reverse()
            print("Path:", " -> ".join(path))
            return

        for neighbor in get_neighbors(word, words):
            new_cost = g[word] + 1
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                parent[neighbor] = word
                h = heuristic(neighbor, goal)
                f = new_cost + h
                print(f"  Checking {neighbor}: g={new_cost}, h={h}, f={f}")
                heapq.heappush(pq, (f, neighbor))

words = [

    "CAT",
    "COT",
    "COG",
    "DOG",
    "DAT",
    "DOT"
]

start = "CAT"
goal = "DOG"

astar(start, goal, words)