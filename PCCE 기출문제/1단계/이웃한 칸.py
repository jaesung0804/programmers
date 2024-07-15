def solution(board, h, w):
    answer = 0
    # 색칠된 격자 보드판
    n = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    
    for j in range(4):
        h_check = h+dh[j]
        w_check = w+dw[j]
        if (0 <= h_check < n) and (0 <= w_check < n) and (color == board[h_check][w_check]):
            answer += 1

    return answer