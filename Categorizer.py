#!/usr/bin/env python
#encoding: utf-8
import json
import os
import random
import sys
import time

from bs4 import BeautifulSoup
import requests


def readURL(URL):
    r = requests.get(URL)
    l = BeautifulSoup(r.content)
    if l.text.encode('utf-8').find('Please wait and try your request again later.') != -1:
        print 'REQUEST DENIED'
        time.sleep(300)
        return ('WAIT','WRONG')
    elif l.text.encode('utf-8').find('There are no listings for this item') != -1:
        return ('WRONG','WRONG')
    data = l.findAll('span')
    curIDs = getCurrencyID(l)
    return (data, curIDs)

def getvalutess():
    infile = open('valute', 'r').read()
    data = json.loads(infile)
    return data

def importLinks(fileName):
    f = open(fileName, 'r')
    data = [i.strip() for i in f.readlines()]
    return data
    
def writeCategorize(url, cat, avg):
    f = open(cat, 'a')
    f.write(str(avg) + ';' + url + '\n')
    f.close()

def getCategory(url):
    if url.find('StatTrak') != -1:
        return 'StatTrak'
    if url.find('Souvenir') != -1:
        return 'Souvenir'
    return 'normal'

def getCurrencyID(html):
    html_to_string = str(html)
    lines = html_to_string.split('\n')
    for i in lines:
        if i.find('currencyid') != -1:
            line = i
            break

    ids = []
    kk = line.split('currencyid')
    del kk[0]
    for k in kk:
        ids.append(k[3:7])
    return ids

def loging(tmp, curID):
    log = open('log','a')
    log.write('{0}\t{1}\n'.format(tmp, curID))
    log.close()

def valutesToEur(tmp, curID):
    #print str(tmp) + ' ' + str(curID)
    if tmp.find('Sold') != -1:
        return 5014.0
    if curID == '2001':
        return (float(tmp.replace('$','').replace('USD',''))/valutes['USD'])
    if curID == '2002':
        return (float(tmp.replace('£',''))/valutes['GBP'])
    if curID == '2003':
        return (float(tmp.replace('€','').replace(',','.'))/valutes['EUR'])
    if curID == '2004':
        return (float(tmp.replace('CHF ',''))/valutes['CHF'])
    if curID == '2005':
        return (float(tmp.split(' ')[0].replace(',','.'))/valutes['RUB'])
    if curID == '2006':
        print curID
        sys.exit()
    if curID == '2007':
        return (float(tmp.split(' ')[1].replace(',',''))/valutes['BRL'])
    if curID == '2008':
        return (float(tmp.split(' ')[1].replace(',','').replace('¥',''))/valutes['JPY'])
    if curID == '2009':
        return (float(tmp.replace(' kr','').replace('.','').replace(',','.'))/valutes['SEK'])
    if curID == '2010':
        return (float(tmp.replace('Rp ','').replace(' ',''))/valutes['IDR'])
    if curID == '2011':
        return (float(tmp.replace('RM','').replace(',',''))/valutes['MYR'])
    if curID == '2012':
        return (float(tmp.replace('P','').replace(',',''))/valutes['PHP'])
    if curID == '2013':
        return (float(tmp.replace('S$',''))/valutes['SGD'])
    if curID == '2014':
        return (float(tmp.replace('฿','').replace(',',''))/valutes['THB'])
    if curID == '2015':
        print curID
        sys.exit()
    if curID == '2016':
        return (float(tmp.replace('₩ ', '').replace(',',''))/valutes['KRW'])
    if curID == '2017':
        return (float(tmp.split(' ')[0].replace(',','.'))/valutes['TRY'])
    if curID == '2018':
        print curID
        sys.exit()
    if curID == '2019':
        return (float(tmp.replace('Mex$ ','').replace(',',''))/valutes['MXN'])
    if curID == '2020':
        return (float(tmp.split(' ')[1].replace(',','.'))/valutes['CAD'])
    if curID == '2021':
        print curID
        sys.exit()
    if curID == '2022':
        return (float(tmp.replace('NZ$ ',''))/valutes['NZD'])
    if curID == '2023':
        return (float(tmp.split(' ')[1].replace(',',''))/valutes['CNY'])
    if curID == '2024':
        return (float(tmp.replace('₹ ','').replace(',',''))/valutes['INR'])
    if curID == '2025':
        return (float(tmp.replace('CLP$', '').replace('.','').replace(',','.'))/valutes['CLP'])
    if curID == '2026':
        return (float(tmp.replace('S/.',''))/valutes['SGD'])
    if curID == '2027':
        return (float(tmp.replace('COL$ ','').replace('.','').replace(',','.'))/valutes['COP'])
    if curID == '2028':
        return (float(tmp.replace('R ','').replace(' ',''))/valutes['ZAR'])
    if curID == '2029':
        return (float(tmp.replace('HK$ ','').replace(',',''))/valutes['HKD'])
    if curID == '2030':
        return (float(tmp.replace('NT$ ','').replace(',',''))/valutes['TWD'])
    if curID == '2031':
        return (float(tmp.replace(' SR', ''))/valutes['SAR'])
    if curID == '2032':
        return (float(tmp.replace(' AED', ''))/valutes['AED'])
    """if curID == '2033':
    if curID == '2034':
    if curID == '2035':
    if curID == '2036':
    if curID == '2037':
    if curID == '2038':
    if curID == '2039':
    if curID == '2040':

    return (float(tmp.split(' ')[0].replace(',','.'))/valutes['RUB'])
    return (float(tmp.replace('฿','').replace(',',''))/valutes['THB'])  
    return (float(tmp.replace('NZ$ ',''))/valutes['NZD'])
    return (float(tmp.replace(' DH', ''))/valutes['AED'])
    """
    print 'SomethingElse', tmp, curID
    loging(tmp, curID)
    return 10000.0

def getPrices(li):
    pli = li
    pli.sort()
    return pli

#####################################################################

links = importLinks('links')

k = 0
#os.system('python Exchanger.py')
valutes = getvalutess()

for t_url in links:
    time.sleep(round(random.uniform(12,13),2))
    if not((k+1) % 50):
        #os.system('python Exchanger.py')
        valutes = getvalutess()

    (span_list, currencyIDs) = readURL(t_url)
    category = getCategory(t_url)

    if span_list == 'WRONG':
        print 'inactive: ', t_url
        f = open('inactive{0}Links'.format(category),'a')
        f.write('0.0;' + t_url + '\n')
        f.close()
        continue
    if span_list == 'WAIT':
        print '--- SLOW ---'
        f = open('slower{0}Link'.format(category),'a')
        f.write('0.0;' + t_url + '\n')
        f.close()
        continue

    values = []
    print k, t_url
    k += 1
    count = -2
    for span in span_list: 
        if span.get('class') is not None:
            if span.get('class')[0] in ['market_listing_price']:
                count += 1
                if(count%3):
                    continue
                value = span.text.encode('utf-8').strip().replace('-','')
                values.append(valutesToEur(value,currencyIDs[count/3]))
                
    prices = getPrices(values)


    if len(prices) == 1 or len(prices) == 2:
        print '{0}\t20+ EUR'.format(category)
        writeCategorize(t_url, '{0}(20+)'.format(category), 25.0)
        continue

    if len(prices) < 3:
        print '{0}\t20+ EUR'.format(category)
        writeCategorize(t_url, '{0}(20+)'.format(category), 25.0)
        continue

    v_avg = round((prices[0] + prices[1] + prices[2]) / 3, 2)
    print v_avg

    if v_avg > 20:
        print '{0}\t20+ EUR'.format(category)
        writeCategorize(t_url, '{0}(20+)'.format(category), v_avg)
        continue

    if v_avg > 15:
        print '{0}\t15-20 EUR'.format(category)
        writeCategorize(t_url, '{0}(15-20)'.format(category), v_avg)
        continue

    if v_avg > 14:
        print '{0}\t14-15 EUR'.format(category)
        writeCategorize(t_url, '{0}(14-15)'.format(category), v_avg)
        continue

    if v_avg > 13:
        print '{0}\t13-14 EUR'.format(category)
        writeCategorize(t_url, '{0}(13-14)'.format(category), v_avg)
        continue

    if v_avg > 12:
        print '{0}\t12-13 EUR'.format(category)
        writeCategorize(t_url, '{0}(12-13)'.format(category), v_avg)
        continue

    if v_avg > 11:
        print '{0}\t11-12 EUR'.format(category)
        writeCategorize(t_url, '{0}(11-12)'.format(category), v_avg)
        continue

    if v_avg > 10:
        print '{0}\t10-11 EUR'.format(category)
        writeCategorize(t_url, '{0}(10-11)'.format(category), v_avg)
        continue

    if v_avg > 9:
        print '{0}\t9-10 EUR'.format(category)
        writeCategorize(t_url, '{0}(9-10)'.format(category), v_avg)
        continue

    if v_avg > 8:
        print '{0}\t8-9 EUR'.format(category)
        writeCategorize(t_url, '{0}(8-9)'.format(category), v_avg)
        continue

    if v_avg > 7:
        print '{0}\t7-8 EUR'.format(category)
        writeCategorize(t_url, '{0}(7-8)'.format(category), v_avg)
        continue

    if v_avg > 6:
        print '{0}\t6-7 EUR'.format(category)
        writeCategorize(t_url, '{0}(6-7)'.format(category), v_avg)
        continue

    if v_avg > 5:
        print '{0}\t5-6 EUR'.format(category)
        writeCategorize(t_url, '{0}(5-6)'.format(category), v_avg)
        continue

    if v_avg > 4:
        print '{0}\t4-5 EUR'.format(category)
        writeCategorize(t_url, '{0}(4-5)'.format(category), v_avg)
        continue

    if v_avg > 3:
        print '{0}\t3-4 EUR'.format(category)
        writeCategorize(t_url, '{0}(3-4)'.format(category), v_avg)
        continue
  
    if v_avg > 2:
        print '{0}\t2-3 EUR'.format(category)
        writeCategorize(t_url, '{0}(2-3)'.format(category), v_avg)
        continue
    
    if v_avg > 1:
        print '{0}\t1-2 EUR'.format(category)
        writeCategorize(t_url, '{0}(1-2)'.format(category), v_avg)
        continue

    print '{0}\t0-1 EUR'.format(category)
    writeCategorize(t_url, '{0}(0-1)'.format(category), v_avg)