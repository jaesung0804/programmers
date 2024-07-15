
def solution(players, callings):
    # 선수의 위치를 저장하는 해시 테이블
    position_map = {name: i for i, name in enumerate(players)}
    
    # 호출 처리
    for name in callings:
        idx = position_map[name]
        
        # 현재 위치의 선수와 바로 앞 위치의 선수와 교체
        # players[idx]는 name이며, players[idx - 1]는 name의 바로 앞 선수
        # 두 선수의 위치를 스왑
        prev_name = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        # 위치 맵 업데이트
        position_map[name] = idx - 1
        position_map[prev_name] = idx
    return players