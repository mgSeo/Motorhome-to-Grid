def func(data):

    import datetime
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse as urlparse


    def get_holiday(url, operation, params, serviceKey):
        params = urlparse.urlencode(params)
        request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
        # session = requests.Session()
        # session.max_redirects = 60

        res = requests.get(request_query, allow_redirects=False)
        soup = BeautifulSoup(res.text, 'lxml')
        items = soup.find_all('item')
        day = pd.DataFrame()
        format = '%Y%m%d'
        for item in items:
            data = item.locdate.get_text()
            date = datetime.datetime.strptime(data,format)
            datedata = {'날짜':date}
            day = day.append(datedata, ignore_index=True)
        return day

    data_time = pd.to_datetime(data['timestamp'].iloc[0])
    year=data_time.year
    
    serviceKey = "HZNNbjGa4DZYv9Jgp3e%2BbIQQ2OcRe%2F%2BwpsNzfp9mr4M6GPyJ%2BDu5Odw3iDJjUhoSDztfhGvnUOoZPcvY3axB5g%3D%3D"
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
    operation = 'getRestDeInfo'
    params = {'solYear':year,"numOfRows":100}
    holidays = get_holiday(url, operation, params, serviceKey) # holidays 는 공휴일 전체 목록

    week = data_time.weekday()+1
    data['week'] = week
    base_day = datetime.timedelta(days=1) # 기준 시간 단위
    
    ### 날짜 분류
    if data_time in holidays:
        holiday = 1
    else:
        holiday = 0
    
    if data_time - base_day in holidays: # 기준 데이터를 기준으로 전일과 후일에 공휴일이 있는지 (공휴일 전후로 패턴 변화가 있을 수 있음.)
        near_holiday = 1
    elif data_time + base_day in holidays:
        near_holiday = 1
    else:
        near_holiday = 0
     
    if holiday == 1:
        data['daytype'] = 1 # 공휴일이다.
    elif  near_holiday == 1:
        if week <= 5:
            data['daytype'] = 2 # 근처 공휴일이 있는 주중
        else:
            data['daytype'] = 3 # 근처 공휴일이 있는 주말
    elif  week<=5:
            data['daytype'] = 4 # 근처 공휴일이 없는 주중 
    else:
        data['daytype'] = 5 # 근처 공휴일이 없는 주말

    return data            
            
        
    

        
    