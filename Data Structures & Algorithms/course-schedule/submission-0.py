class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]

        for v,w in prerequisites:
            graph[v].append(w)

        UNVISITED, VISITING, VISITED = 0, 1 ,2 
        state = [UNVISITED] * numCourses

        def has_cycle(node):
            if state[node] == VISITED:
                return False

            if state[node] == VISITING:
                return True

            state[node] = VISITING

            for v in graph[node]:
                if has_cycle(v):
                    return True

            state[node] = VISITED
            return False


        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True


        
        