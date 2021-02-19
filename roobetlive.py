import json
import requests
import math
data = ""
lastID = ""
def initialize():
     f= open("output.json")
     jsondata = f.read()
     global data
     data = json.loads(jsondata)
     workLive()
def getPoints(a,b,c):
    total = 0
    total += a - 2
    total += b - 2
    total += c - 2
    return total
def workLive():
    global lastID
    while (True):
        url = "https://api.roobet.com/crash/recentNumbers"
        r = requests.get(url)
        activeGame = r.json()
        if (activeGame[0]['id'] == lastID):
            continue
        else:
            lastID = activeGame[0]['id']
            total = getPoints(activeGame[0]['crashPoint'],activeGame[1]['crashPoint'],activeGame[2]['crashPoint'])
            point = math.floor(total)-20
            if (point > len(data)-1):
                point = len(data)-1
            print(data[point])

initialize()