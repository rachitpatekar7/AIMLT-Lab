from collections import deque

def bfs_maze_solver(maze, s, e):
    r, c = len(maze), len(maze[0])
    q = deque([(s, [s])]) 
    v = set()
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while q:
        (cur, p) = q.popleft()
        if cur == e:
            return p

        for direction in d:
            nr, nc = cur[0] + direction[0], cur[1] + direction[1]
            if 0 <= nr < r and 0 <= nc < c and maze[nr][nc] == 0:
                nxt = (nr, nc)
                if nxt not in v:
                    q.append((nxt, p + [nxt]))
                    v.add(nxt)
    return None
#sample maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
s = (0, 0)
e = (4, 4)
print(maze)
print(s)
print(e)
path = bfs_maze_solver(maze, s, e)
print("BFS Path:", path)
