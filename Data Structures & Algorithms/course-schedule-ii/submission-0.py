from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque([n for n in range(numCourses) if indegree[n] == 0])

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []

        