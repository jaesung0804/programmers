import re

def solution(dartResult):
    answer = 0
    
    score = re.compile("(\d+)[S,D,T][*,#]?")
    square = re.compile("\d+([S,D,T])[*,#]?")
    award = re.compile("\d+[S,D,T]([*,#]?)")
    
    scores = score.findall(dartResult)
    squares = square.findall(dartResult)
    awards = award.findall(dartResult)
    
    square_dict = {x:i+1 for i,x in enumerate(['S','D','T'])}
    
    for i in range(3):
        stage_score = int(scores[i]) ** square_dict[squares[i]]
        if awards[i] == '#':
            stage_score = (-1)*stage_score
        elif awards[i] == '*':
            stage_score = stage_score * 2
        
        if i<= 1:
            if awards[i+1] == '*':
                stage_score = stage_score * 2
                
        answer += stage_score
    return answer