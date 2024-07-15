def solution(name, yearning, photo):
    answer = []
    
    score_dict = dict(zip(name,yearning))
    
    score = 0
    for p in photo:
        for man in p:
            if man in name:
                score += score_dict[man]
        answer.append(score)
        score = 0
    return answer