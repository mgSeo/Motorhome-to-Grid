## parameters ############################
Foldername = '10015_20220417-20220517'
Carname = '10015'
## pre-set ############################
from numpy import r_
import pandas as pd
Start_day = Foldername[-17:-9]
End_day = Foldername[-8:]
dt_index = pd.date_range(start=Start_day, end=End_day)
dt_list = dt_index.strftime("%Y%m%d").tolist()
index = ['clientid','timestamp','cell1','cell2','cell3','cell4','cell_cap',\
            'current1','current2','current3','current4','etc','port1','port2','rport','saac','sac','soc','state',\
                'temperature1','temperature2','temperature3','temperature4','temperature5','temperature6','timeindex','version','volt','wport']
## pre-set ############################



for day in range(len(dt_list)):
    # if day != 3:
    #     continue
    Filename = 'Datas/' + Foldername + '/' + Carname + '-bms_records-' + dt_list[day] + '.csv'    
    Data = pd.read_csv(Filename)
    

    ### 데이터 전처리
    import Preprocess
    data = Preprocess.func(Data,index)

    ### load 분리
    import Disaggregator
    data,r_index = Disaggregator.func(data,index)
    
    ### 요일 및 휴일 반영
    import select_daytype
    data = select_daytype.func(data)

    ### load, PV 시계열로 출력
    import Combine_15min as C15
    data15 = C15.func(data,r_index)

    data15.to_csv('min15_'+dt_list[day]+'.csv')
    ss=1

