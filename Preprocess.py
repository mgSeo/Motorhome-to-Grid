def func(Data,index):
        # re-indexing, index 에러있음
        Data.columns = index
        # SoC outlier 제거
        data = Data[(Data['soc'] >= 0) & (Data['soc'] <= 100)]
        
        # wport (베이런 640)
        port_len = 86
        data.drop(['port1'], axis=1, inplace=True) # port 1 삭제
        data.drop(['port2'], axis=1, inplace=True) # port 2 삭제
        data.drop(['rport'], axis=1, inplace=True) # rport 삭제
        data['wport'] = data['wport'].str.strip() # str 앞 공백 제거        
        idx = data.index[data['wport'].str.len() < port_len].tolist() # port 끝 생략된거 찾기
        if len(idx) > 0:
                data['wport'][idx] = data['wport'][idx].str.ljust(width=port_len, fillchar='0') # 빈 곳 0으로 채우기
        for p in range(43):
                ports = "port{}".format(p)
                data[ports] = data['wport'].str.slice(start=p*2, stop=(p+1)*2) # 인덱스 사이 값 반환
        return data