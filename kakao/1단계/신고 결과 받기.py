def solution(id_list, report, k):
    reports_by_user = {user: set() for user in id_list}
    reported_count = {user: 0 for user in id_list}
    
    for rep in set(report):
        reporter, reported = rep.split()
        reports_by_user[reporter].add(reported)
    
    for reporter in reports_by_user:
        for reported in reports_by_user[reporter]:
            reported_count[reported] += 1
    
    answer = [0] * len(id_list)
    for idx, user in enumerate(id_list):
        mail_count = 0
        for reported in reports_by_user[user]:
            if reported_count[reported] >= k:
                mail_count += 1
        answer[idx] = mail_count
    
    return answer