import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(
    'mongodb+srv://TCK:Thun@cluster0.d0inr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
col = client['siam']['location']
location = [x for x in col.find()]
food = client['siam']['food']
find_food = [x for x in food.find()]
hotel = client['siam']['hotel']
find_hotel = [x for x in hotel.find()]
latlong = client['siam']['latlong']
data = [x for x in latlong.find()]
other = client['siam']['other-activity']
find_other = [x for x in other.find()]
print('database connected success')


def getLatLong(title):
    lat = 0
    long = 0
    for i in data:
        if i["title"] == title:
            lat = i["latitude"]
            long = i["longtitude"]
    return lat, long


def getFood():
    return find_food


def getHotel():
    return find_hotel


def getData():
    return location


def getOther():
    return find_other


def searchByName(name):
    query = []
    for p in location:
        if name.lower() in p['title'].lower():
            query += [p]
    # print(query)
    return query


def searchByType(type):
    query = []
    for p in location:
        if type in p['type']:
            query += [p]
    return query


getOther()
