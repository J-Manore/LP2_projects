arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    min_idx = i

    print(f"\nPass {i+1}")

    for j in range(i + 1, n):

        print(f"Comparing {arr[j]} and {arr[min_idx]}")

        if arr[j] < arr[min_idx]:
            min_idx = j

    print(f"Swapping {arr[i]} and {arr[min_idx]}")

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print("Array:", arr)

print("\nSorted array:", arr)


import heapq

graph = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}


def dijkstra(start):

    pq = [(0, start)]
    dist = {start: 0}

    while pq:

        d, node = heapq.heappop(pq)

        print(f"\nVisiting {node} with distance {d}")

        for neighbor, weight in graph[node]:

            new_dist = d + weight

            print(f"Checking {neighbor}: {d} + {weight} = {new_dist}")

            if neighbor not in dist or new_dist < dist[neighbor]:

                dist[neighbor] = new_dist

                print(f"  Updating distance of {neighbor} to {new_dist}")

                heapq.heappush(pq, (new_dist, neighbor))

    return dist


print("\nShortest Distances:", dijkstra("A"))


import heapq

graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 1)],
    "C": [("A", 3), ("B", 1), ("D", 4)],
    "D": [("B", 1), ("C", 4)],
}


def prim(start):

    visited = set()
    pq = [(0, start)]
    cost = 0

    while pq:

        w, node = heapq.heappop(pq)

        if node not in visited:

            print(f"Adding node {node} with edge cost {w}")

            visited.add(node)

            cost += w

            for neighbor, weight in graph[node]:

                if neighbor not in visited:

                    print(f"  Considering edge {node}-{neighbor} : {weight}")

                    heapq.heappush(pq, (weight, neighbor))

    return cost


print("\nMST Cost:", prim("A"))


jobs = [("A", 2, 100), ("B", 1, 50), ("C", 2, 10), ("D", 1, 20)]

# sort by profit descending
jobs.sort(key=lambda x: x[2], reverse=True)

print("Jobs sorted by profit:")
print(jobs)

result = []

for job in jobs:

    print(f"\nSelecting Job {job[0]} with profit {job[2]}")

    result.append(job[0])

print("\nJob order:", result)
