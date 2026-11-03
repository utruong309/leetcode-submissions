class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Input: 
        - numCourses: int, # of courses labeled from 0 to numCourses - 1 
        - prereqs[i] = [ai, bi]: must take course bi before course ai 
        Output: 
        Return the ordering of courses to finish all courses
        If impossible, return an empty array 
        Approach: Topological sort 
        graph: adj list {course: [courses that have it as prereq]}
        indegree: arr of size numCourses 
        indegree[i] = # of ith course's prereqs
        take courses that have no prereqs first - indegree = 0 
        push to queue 
        every course in graph[course] indegree -= 1 because we have taken 1 of their prereqs
        if # of prereqs = 0 -> push to queue to process next 
        a course popped from queue means it can be taken now -> add to result 
        if len(result) != numCourses -> return empty array
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses 
        res = [] 

        for a, b in prerequisites: 
            graph[b].append(a)
            indegree[a] += 1 
        
        queue = deque() 

        for i in range(len(indegree)): 
            if indegree[i] == 0: 
                queue.append(i)
        
        while queue: 
            current = queue.popleft() 
            res.append(current)

            for nxt in graph[current]: 
                indegree[nxt] -= 1 

                if indegree[nxt] == 0: 
                    queue.append(nxt)
        
        if len(res) != numCourses: 
            return [] 
        
        return res 