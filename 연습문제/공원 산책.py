def solution(park, routes):
    H = len(park)
    W = len(park[0])
    start_y, start_x = None, None
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start_y, start_x = i, j
                break
        if start_y is not None:
            break
    
    for route in routes:
        direction, step_size = route.split()
        step_size = int(step_size)
        dy, dx = 0, 0
        if direction == 'E':
            dx = 1
        elif direction == 'W':
            dx = -1
        elif direction == 'S':
            dy = 1
        elif direction == 'N':
            dy = -1
        
        for step in range(1, step_size + 1):
            new_y, new_x = start_y + dy * step, start_x + dx * step
            if 0 <= new_y < H and 0 <= new_x < W:
                if park[new_y][new_x] == 'X':
                    break
            else:
                break
        else:
            start_y, start_x = new_y, new_x
    
    return [start_y, start_x]