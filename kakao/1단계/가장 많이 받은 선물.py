def solution(friends, gifts):
    gift_dict = {friend:0 for friend in friends}
    indices_dict = {friend:0 for friend in friends}
    
    for gift in gifts:
        give, receive = gift.split()
        indices_dict[give] += 1
        indices_dict[receive] -= 1
    
    str_list = []
    for f in friends:
        for ff in friends:
            str_list.append(f+" "+ff)
    
    tmp = []
    for gift in list(set(str_list)):
        if gift not in tmp:
            give, receive = gift.split()
            if gifts.count(gift) > gifts.count(receive+" "+give):
                gift_dict[give] += 1
            elif gifts.count(gift) < gifts.count(receive+" "+give):
                gift_dict[receive] += 1
            else:
                if indices_dict[give] > indices_dict[receive]:
                    gift_dict[give] += 1
                elif indices_dict[give] < indices_dict[receive]:
                    gift_dict[receive] += 1
                    
        tmp.append(receive+" "+give)
    #지금 선물 서로 안 주고받았을 때도 선물지수로 인해 들어가는 선물이 빠짐
    return max(gift_dict.values())