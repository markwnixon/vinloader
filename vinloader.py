import sys
import datetime
from scrapers import vinscraper

today=datetime.date.today()

def numbercars(orderid):
    adata=Autos.query.filter(Autos.Orderid==orderid).all()
    ncars=len(adata)
    return ncars

try:
    longs = open('vins.txt').read()
    vlist = longs.split()
except:
    vlist=[]

k=len(vlist)
for j,vin in enumerate(vlist):
    if len(vin)==18:
        vin=vin[1:18]
    if len(vin)==17:
        #try:
        year,make,model,wt,price,navg=vinscraper(vin)

        #except:
            #print(vin,' is not a valid vin')

        lvin=len(vin)
        vin5=vin[lvin-5:lvin]
        if year is not None:
            print(vin, len(vin), year, make, model, wt, price, navg)

    print('Completed iteration: ',j+1,' of ',k)

sys.exit('All VINS executed...code completed')
