def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
    word_dict = {word:str(i) for i,word in enumerate(word_list)}
    
    for word in word_list:
        s = s.replace(word, word_dict[word])
    
    return int(s)