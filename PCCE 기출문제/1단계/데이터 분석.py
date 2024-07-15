def solution(data, ext, val_ext, sort_by):
    
    ext_dict = {"code":0, "date":1, "maximum":2, "remain":3}
    
    raw_data = [d for d in data if int(d[ext_dict[ext]]) < val_ext]
    raw_data.sort(key = lambda x:x[ext_dict[sort_by]])

    return raw_data