from service.database import getData

location = getData()
data = []
for i in location:
    print(i["title"])
    latlong = input().split(",")
    data += [
        {
            "title": i["title"],
            "latitude": latlong[0],
            "longtitude": latlong[1]
        }
    ]


print(data)
