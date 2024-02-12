from components.carousel import showCarousel
from service.database import searchByName
from service.render import renderCard


def responseSearch(message):
    place_name = message["queryResult"]["parameters"]["place_name"]
    print("place_name: ", place_name)
    data = searchByName(place_name)
    card = renderCard(data)
    
    if searchByName(place_name) == []:
        print("place not found")
        return {"fulfillmentText": "place not found"}
    else:
    
        return showCarousel(card)
