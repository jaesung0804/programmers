def solution(survey, choices):
    answer = ''
    type_list = ["R","T","C","F","J","M","A","N"]
    score_dict = {x:0 for x in type_list}
    
    for s,c in zip(survey, choices):
        if c >= 4:
            score_dict[s[1]] += (c-4)
        else: score_dict[s[0]] += (4-c)
    
    for i in range(4):
        if score_dict[type_list[2*i]] >= score_dict[type_list[2*i + 1]]:
            answer += type_list[2*i]
        else: answer += type_list[2*i + 1]
    
    return answer