def solution(bandage, health, attacks):
    # 붕대 감으면 t초마다 x만큼 체력 회복
    
    # t초 연속으로 붕대 감는데 성공하면 y만큼의 체력 추가 회복
    
    # 체력 회복은 최대 체력까지만 가능
    
    # 공격당하면 붕대 취소, 끝나는대로 즉시 붕대감기 다시 시작, 체력 0이하면 뒤짐
    
    
    
    att_map = {att[0]:att[1] for att in attacks}
    init_health = health
    time = 0
    heal_time = 0
        
    
    for j in range(attacks[-1][0]):
        time += 1
        heal_time += 1
            
        health += bandage[1]
            
        if time in att_map.keys():
            health -= (att_map[time] + bandage[1])
            heal_time = 0
        
        
        if heal_time == bandage[0]:
            health += bandage[2]
            heal_time = 0
    
            
        if health >= init_health :
            health = init_health
        elif health <= 0 :
            health = -1
            break
    
    return health