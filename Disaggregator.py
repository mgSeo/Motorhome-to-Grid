from statistics import mean


def func(data,index):
    import numpy as np
    import pandas as pd
    pd.set_option('mode.chained_assignment',  None)
    
    # data -> load[A], gen[A], alter[A]
    data['load'] = np.zeros([len(data),1])
        
    idx = data[abs(data['current1']) <= 50].index.tolist()
    if len(idx) > 0: # |Current1| <= 50
        data['load'][idx] = data['current1'][idx] - data['current2'][idx]- data['current4'][idx]

    idx = data[abs(data['current1']) > 50].index.tolist()
    if len(idx) > 0: # |Current1| > 50
        data['load'][idx] = data['current3'][idx] - data['current2'][idx]- data['current4'][idx]

    # for t in range(len(data)):
    #     if abs(np.mean([data['current1'][t],data['current3'][t]])) <= 50:
    #         data['load'][t] = data['current1'][t] - data['current2'][t]- data['current4'][t]
    #     else:
    #         data['load'][t] = data['current3'][t] - data['current2'][t]- data['current4'][t]

    data.drop(['current1'], axis=1, inplace=True)
    data.drop(['current3'], axis=1, inplace=True)
    re_index = index
    re_index.remove('current1')
    re_index.remove('current3')
    re_index.append('load')
    return data,re_index