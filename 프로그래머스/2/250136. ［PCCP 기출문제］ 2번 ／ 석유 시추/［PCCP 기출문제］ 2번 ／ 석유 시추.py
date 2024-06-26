from collections import deque
# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = [0 for _ in range(m + 1)]
    
    # 석유 덩이리 값 추출
    def bfs(x,y):
        dq = deque()
        dq.append((x,y))
        cnt = 0;
        visited[x][y] = True
        min_y, max_y = y,y

        while dq:
            x,y = dq.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    dq.append((nx,ny))
        #석유 덩어리의 구역을 최소, 최대 y좌표를 구하여 덩어리값을 result[i]에 저장          
        for i in range(min_y, max_y + 1):
            result[i] += cnt

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)

    
    return max(result)


    