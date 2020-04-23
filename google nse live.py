import requests,time,os,threading
from datetime import datetime

class Stock(threading.Thread):
    def __init__(self,sy):
        threading.Thread.__init__(self)
        self.sy=sy

    def run(self):
        sym=self.sy
        url='https://www.google.com/search?hl=en&q=NSE:%20+'+sym
        #url='https://www.google.com/search?source=hp&ei=XyaZXvHFN5Sd4-EPueG22AI&q=axis+share&oq=axis+share&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABCDATICCAAyAggAMgIIADICCAAyBAgAEAoyAggAMgIIAEojCBcSHzBnMTEyZzE2NmcxMjJnMTQ1ZzM4NGcwZzExMmcxMDdKFQgYEhEwZzFnMWcxZzFnMWcwZzFnMVDflwFY1KQBYP6lAWgAcAB4AIAB_QKIAdwIkgEHMC42LjAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwix8bOOxu7oAhWUzjgGHbmwDSsQ4dUDCAc&uact=5'
        headers ={"User-Agent": 'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.66 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        try:
            page = requests.get(url,headers=headers)
            p=str(page.content)
            a=p.split('vWLAgc">')
            a=a[1].split('</span>')
            a=a[0]
            print(sym+" "+str(a)+"\n")                
        except:
            url='https://www.google.com/search?source=hp&ei=XyaZXvHFN5Sd4-EPueG22AI&q=axis+share&oq=axis+share&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABCDATICCAAyAggAMgIIADICCAAyBAgAEAoyAggAMgIIAEojCBcSHzBnMTEyZzE2NmcxMjJnMTQ1ZzM4NGcwZzExMmcxMDdKFQgYEhEwZzFnMWcxZzFnMWcwZzFnMVDflwFY1KQBYP6lAWgAcAB4AIAB_QKIAdwIkgEHMC42LjAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwix8bOOxu7oAhWUzjgGHbmwDSsQ4dUDCAc&uact=5'
            try:
                page = requests.get(url,headers=headers)
                p=str(page.content)
                a=p.split('vWLAgc">')
                a=a[1].split('</span>')
                a=a[0]
                print(sym+" "+str(a)+"")
            except:
                print("Error in connecting")
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
    mm=Stock('M&M')
    mm.start()
    cip=Stock('CIPLA')
    cip.start()
    rel=Stock('RELIANCE')
    rel.start()
    time.sleep(10)
