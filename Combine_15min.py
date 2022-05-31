def func(data,index):
    import numpy as np
    import pandas as pd
    re_data = pd.DataFrame(np.zeros([96,len(index)]),columns=index)
    re_data = pd.DataFrame()    
    data['timestamp'] = pd.to_datetime(data['timestamp']) # datetime type으로 변환
    data.index = data['timestamp'] # index 로 설정
    # mean
    lists = ['cell1','cell2','cell3','cell4','volt']
    for l in range(len(lists)):
        re_data[lists[l]] = data[lists[l]].resample('15T').mean()
    # sum
    lists = ['pv','load']
    for l in range(len(lists)):
        re_data[lists[l]] = data[lists[l]].resample('15T').sum()
    # median
    lists = ['cell_cap']
    for l in range(len(lists)):
        re_data[lists[l]] = data[lists[l]].resample('15T').median()
    # last
    lists = ['clientid','soc','sac','state']
    for l in range(len(lists)):
        re_data[lists[l]] = data[lists[l]].resample('15T').last()
    # port
    for p in range(43):
        ports = "port{}".format(p)
        re_data[ports] = data[ports].resample('15T').sum()
    return re_data