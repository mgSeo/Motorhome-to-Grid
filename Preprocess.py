def func(Data,index):
        # re-indexing, index 에러있음
        Data.columns = index
        # SoC outlier 제거
        data = Data[(Data['soc'] >= 0) & (Data['soc'] <= 100)]
        # data[data['port1'] <= 0.1] = int(0)
        # data[data['port2'] <= 0.1] = int(0)

        return data