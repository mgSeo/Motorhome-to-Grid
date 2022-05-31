# import numpy as np
import pandas as pd

Foldernames = ['10015_20220417-20220517', 'VABJ0052_20220417-20220517', 'VABJ0079_20220417-20220517','VABJ0099_20220301-20220530']
cars = ['10015', 'VABJ0052', 'VABJ0079','VABJ0099']
Path = 'Result_accumulated/'
for car in range(len(cars)):
    ## parameters ############################
    Foldername = Foldernames[car]
    Carname = cars[car]
    ## pre-set ############################    
    Start_day = Foldername[-17:-9]
    End_day = Foldername[-8:]
    dt_index = pd.date_range(start=Start_day, end=End_day)
    dt_list = dt_index.strftime("%Y%m%d").tolist()
    index = ['clientid','timestamp','cell1','cell2','cell3','cell4','cell_cap',\
                'current1','current2','current3','current4','etc','port1','port2','rport','saac','sac','soc','state',\
                    'temperature1','temperature2','temperature3','temperature4','temperature5','temperature6','timeindex','version','volt','wport']
    ## pre-set ############################


    df = pd.DataFrame() # df: 15분 데이터 적층용 데이터프레임
    for day in range(len(dt_list)):
        Filename = 'Datas/' + Foldername + '/' + Carname + '-bms_records-' + dt_list[day] + '.csv'    
        Data = pd.read_csv(Filename)
        
        ### 데이터 전처리
        import Preprocess
        data = Preprocess.func(Data,index)

        ### load 분리
        import Disaggregator
        data,r_index = Disaggregator.func(data,index)

        ### load, PV 시계열로 출력
        import Combine_15min as C15
        data15 = C15.func(data,r_index)

        ### 적층적층
        df = pd.concat([df,data15])
    df.to_csv(Path + Carname+'_Accumulated_15min_datas.csv')