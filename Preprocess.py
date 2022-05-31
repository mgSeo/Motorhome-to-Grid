def func(Data,index):
        # re-indexing, index 에러있음
        Data.columns = index
        # SoC outlier 제거
        data = Data[(Data['soc'] >= 0) & (Data['soc'] <= 100)]
        
        # wport (베이런 640)
        data.drop(['port1'], axis=1, inplace=True) # port 1 삭제
        data.drop(['port2'], axis=1, inplace=True) # port 2 삭제
        data['wport'] = data['wport'].str.strip() # str 앞 공백 제거        
        idx = data['wport'][data['wport'].str.len() < 86].tolist() # port 끝 생략된거 찾기
        if len(idx) > 0:
                sss=1
        for p in range(43):
                if p==33:
                        ss=1
                ports = "port{}".format(p)
                data[ports] = data['wport'].str.slice(start=p*2, stop=(p+1)*2) # 인덱스 사이 값 반환

        return data