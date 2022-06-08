def func(data):

    import datetime
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse as urlparse


    def get_holiday(url, operation, params, serviceKey):
        params = urlparse.urlencode(params)
        request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
        res = requests.get(request_query)
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
    holidays = get_holiday(url, operation, params, serviceKey)

    week=data_time.weekday()+1
    data['week']=week
    base_day=datetime.timedelta(days=1)
    
    
    
    
    
    
    
    
    if data_time in holidays:
        holiday=1
    else:
        holiday=0
    
    if data_time-base_day in holidays:
        near_holiday=1
    elif data_time+base_day in holidays:
        near_holiday=1
    else:
        near_holiday=0
     
    if holiday==1:
        data['daytype']=1
    elif  near_holiday==1:
        
        if week<=5:
            data['daytype']=2
        else:
            data['daytype']=3
    elif  week<=5:
            data['daytype']=4
    else:
        data['daytype']=5
    

    return data            
            
        
    

        
    