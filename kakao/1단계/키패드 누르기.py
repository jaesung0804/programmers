def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_now = keypad['*']
    right_now = keypad['#']

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_now = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_now = keypad[number]
        else:
            target_pos = keypad[number]
            dist_l = abs(left_now[0] - target_pos[0]) + abs(left_now[1] - target_pos[1])
            dist_r = abs(right_now[0] - target_pos[0]) + abs(right_now[1] - target_pos[1])

            if dist_l < dist_r:
                answer += 'L'
                left_now = target_pos
            elif dist_l > dist_r:
                answer += 'R'
                right_now = target_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    left_now = target_pos
                else:
                    answer += 'R'
                    right_now = target_pos

    return answer