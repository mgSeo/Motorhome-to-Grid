def func(data,index):
    import numpy as np
    import pandas as pd
    re_data = pd.DataFrame(np.zeros([96,len(index)]),columns=index)
    re_data = pd.DataFrame()

    ###
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.index = data['timestamp'] # index 
    re_data['clientid'] = data.clientid.resample('15T').last()
    re_data['cell1'] = data.cell1.resample('15T').mean()
    re_data['cell2'] = data.cell2.resample('15T').mean()
    re_data['cell3'] = data.cell3.resample('15T').mean()
    re_data['cell4'] = data.cell4.resample('15T').mean()
    re_data['volt'] = data.volt.resample('15T').mean()    
    re_data['pv'] = data.current4.resample('15T').sum()
    re_data['load'] = data.load.resample('15T').sum()
    re_data['cell_cap'] = data.cell_cap.resample('15T').median()
    re_data['soc'] = data.soc.resample('15T').last()
    re_data['sac'] = data.sac.resample('15T').last()
    re_data['state'] = data.state.resample('15T').last()
    ### 수정 필요@@@@@@@@@@@
    re_data['port1'] = data.port1.resample('15T').last()
    re_data['port2'] = data.port2.resample('15T').last()
    re_data['rport'] = data.rport.resample('15T').last()
    re_data['wport'] = data.wport.resample('15T').last()
    ###@@@@@@@@@@@@@@@@@@@@
    
    return re_data
