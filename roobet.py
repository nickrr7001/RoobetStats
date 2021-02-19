import requests
import math
import time
import json
analysis = dict()
datapoints = 0
ranges = []
existingIDs = [] 
def getRecentNumbers():
    url = "https://api.roobet.com/crash/recentNumbers"
    r = requests.get(url)
    return r.json()
def getPoints(a,b,c):
    total = 0
    total += a - 2
    total += b - 2
    total += c - 2
    return total
def sectionPoints():
    global datapoints
    while (datapoints < 1000):
        data = getRecentNumbers()
        i = len(data) - 1
        iter = 0
        a = 0
        b = 0
        c = 0
        while( i >= 0):
            if (iter == 3):
                iter = 0
                total = math.floor(getPoints(a,b,c))
                result = "Under"
                if (float(data[i]['crashPoint']) >= 2):
                    result = "Over"
                analysis.update({total:result})
                if (total > 30):
                    ranges[29].append(result)
                elif (total < -20):
                    ranges[0].append(result)
                else:
                    ranges[total - 20].append(result)
            if (iter == 0):
                a = float(data[i]['crashPoint'])
            elif (iter == 1):
                b = float(data[i]['crashPoint'])
            else:
                c = float(data[i]['crashPoint'])
            iter+=1
            i-=1
        datapoints += 1
        print("Datapoint: " + str(datapoints))
        time.sleep(5)
    print(analysis)
    averages = [None] * 50
    iter = 0
    for i in ranges:
        if (i == []):
            iter += 1
            continue
        under = 0
        over = 0
        for j in i:
            if (j == "Over"):
                over += 1
            else:
                under += 1
        if (over > under):
            if (over != 0 or under != 0):
                percentage = over/(over+under)
            else:
                percentage = 0
            averages[iter] = "Over " + str(percentage)
        else:
            if (over != 0 and under != 0):
                percentage = under/(over+under)
            else:
                percentage = 0
            averages[iter] = "Under " + str(percentage)
        iter+=1
    for i in range(len(averages)):
        print (i-20)
        print (averages[i])
    jsonData = json.dumps(averages)
    f = open("output.json","w")
    f.write(jsonData)
    f.close()
            
def lastThree():
    data = getRecentNumbers()
    print(getPoints(float(data[0]['crashPoint']),float(data[1]['crashPoint']),float(data[2]['crashPoint'])))
def setup():
    for i in (range(50)):
        ranges.append([])
    sectionPoints()
setup()