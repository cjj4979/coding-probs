class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visit = {}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            if curr.val not in visit:
                visit[curr.val] = Node(curr.val, [])
            for neighbor in curr.neighbors:
                if neighbor.val not in visit:
                    visit[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visit[curr.val].neighbors.append(visit[neighbor.val])
        return visit[1]
