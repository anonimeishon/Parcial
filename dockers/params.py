from datetime import datetime
from pytz import timezone    

def time():
    cartagena = timezone('US/Eastern')
    sa_time = datetime.now(cartagena)
    return (sa_time.strftime('%Y-%m-%d_%H:%M:%S'))

import urllib.request, json 



def temperatura():
    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=3687238&appid=9583c3b4fa60a5323f4d1d115a5f2592") as url:
        data = json.loads(url.read().decode())
        return(data["main"]["temp"]-273.15)



def getparams():
    t = time()
    temp = temperatura()
    return(t,temp)
if __name__ == '__main__':
    print(getparams())