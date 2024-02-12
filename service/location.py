
from components.latlongcard import latLongCard
from service.database import getLatLong


def locationService(message):
    place_title = message["queryResult"]["parameters"]["place_title"]
    print("place title: ", place_title)
    latlong = getLatLong(place_title)

    return latLongCard(place_title, latlong[0], latlong[1])
