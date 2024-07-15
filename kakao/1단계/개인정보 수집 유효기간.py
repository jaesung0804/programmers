def solution(today, terms, privacies):
    answer = []
    today = [int(string) for string in today.split(".")]
    terms = {term.split(" ")[0] : int(term.split(" ")[1]) for term in terms}
    
    for i,p in enumerate(privacies):
        p_day, p_type = [int(string) for string in p.split(" ")[0].split(".")], p.split(" ")[1]
        
        year_diff = today[0] - p_day[0]
        month_diff = today[1] - p_day[1]
        day_diff = today[2] - p_day[2]
        
        
        if (year_diff * 28 * 12 + month_diff * 28 + day_diff) >= (terms[p_type] * 28):
            answer.append(i+1)

    return answer