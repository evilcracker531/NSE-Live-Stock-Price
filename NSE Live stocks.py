import requests,time,os,threading
from datetime import datetime


class Stock(threading.Thread):
    def __init__(self,sy):
        threading.Thread.__init__(self)
        self.sy=sy

    def run(self):
        sym=self.sy
        url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+sym
        headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        try:
            page = requests.get(url,headers=headers)
            p=str(page.content)
            a=p.find('<div id="responseDiv" style="display:none">')+91
            b=p.find('"}')
            sub=p[a:b]

            y=str(sub).split('lastPrice":"')
            y=float(y[1])
            if(sym=='M%26M'):
                sym="M & M"
            h=sym+"  "+str(y)
            print(h)
        except:
            print("Error in Connecting")
        

def gettime():
    time=datetime.now()
    return time.strftime("%H:%M:%S")

while(1):
    print("\n\t\t\t\t\t\tPrice at "+str(gettime())+"\n")
    hdfc=Stock('HDFCBANK')
    hdfc.start()
    axis=Stock('AXISBANK')
    axis.start()
    apollo=Stock('APOLLOTYRE')
    apollo.start()
    kvb=Stock('KARURVYSYA')
    kvb.start()
    yes=Stock('YESBANK')
    yes.start()
    iob=Stock('IOB')
    iob.start()
    tata=Stock('TATAMOTORS')
    tata.start()
    mm=Stock('M%26M')
    mm.start()
    time.sleep(10)
