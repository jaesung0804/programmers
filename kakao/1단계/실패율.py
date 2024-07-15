# def solution(N, stages):
    
#     rate_list = []
#     for i in range(1, N+1):
#         fail = sum(list(map(lambda x:x==i, stages)))
#         touch = sum(list(map(lambda x:x>=i, stages))) 
        
#         if touch == 0:
#             rate = 0
#         else: rate = fail / touch
        
#         rate_list.append(rate - (1e-9)*i)
        
#     sorted_list = sorted(rate_list, reverse = True)
        
#     answer = [rate_list.index(x) + 1 for x in sorted_list]
        
#     return answer

def solution(N, stages):
    stage_count = [0] * (N + 2)
    for stage in stages:
        stage_count[stage] += 1

    players_reached = len(stages)
    fail_rates = []
    
    for i in range(1, N + 1):
        if players_reached == 0:
            fail_rate = 0
        else:
            fail_rate = stage_count[i] / players_reached
        
        fail_rates.append((fail_rate, i))
        players_reached -= stage_count[i]

    fail_rates.sort(key=lambda x: (-x[0], x[1]))

    answer = [stage for _, stage in fail_rates]
    
    return answer