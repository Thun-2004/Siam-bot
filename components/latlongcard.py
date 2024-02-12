def latLongCard(title, lat, long):
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "address": "2194 ถนน เจริญกรุง แขวง วัดพระยาไกร เขตบางคอแหลม กรุงเทพมหานคร 101200",
                        "title": title,
                        "latitude":lat,
                        "type": "location",
                        "longitude": long
                    }
                }
            }
        ]
    }
