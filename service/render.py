from components.card import showCard
from components.card_food import showcardFood
from components.card_hotel import showcardAccom
from components.carousel import showCarousel
from components.quickreplies import quickReply
from service.database import getFood, getHotel


def renderCard(data):
    card = []
    for i in data:
        card += [showCard(i["title"], i["subtitle"],
                          i["imageUri"], i["postback"], i["price"])]
        # test = json.dumps(showCard(place["title"],place["subtitle"]), indent=4)
        # print(test)
    return card


def renderQuickReply(description, data):
    items = []
    # types = list(set([item["type"][0] for item in data]))
    # types = set()
    # for item in data:
    #     type = types.union(set(item["type"]))

    for item in data:
        items += [
            {
                "type": "action",
                "imageUrl": "",
                "action": {
                    "type": "message",
                    "label": item,
                    "text": item
                },
            }
        ]

    return quickReply(description, items)


def renderFoodCard(selection):
    data = getFood()
    cards = []
    a = []
    count = 0
    score = 0
    for food in data:
        count += 1

        if selection[0] in food["type"]:
            score += 2
        if selection[1] in food["type"]:
            score += 3
        if selection[2] in food["meal"]:
            score += 1
        if selection[3] in food["price"]:
            score += 1
# if first two not match
        if score > 4:
            a += [[food["name"], score]]
            cards += [showcardFood(food["name"], food["location"],
                                   food["imgUri"], food["postback"])]
        score = 0
    print(a)
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "flex",
                                "altText": "This is a Flex Message",
                                # bring JSON payload here
                                "contents": {
                                    "type": "carousel",
                                    "contents": cards[0:count]
                                }
                    }
                }
            }
        ]}


def renderAccom(selection):
    data = getHotel()
    cards = []
    count = 0
    for i in data:
        if selection[0] in i["type"] and selection[1] in i["price"]:
            price = ' to '.join(i["price"])
            cards += [showcardAccom(i["name"], i["imgurl"],
                                    i["web"], price, i["location"])]
            count += 1
    print("Accom render success")

    return showCarousel(cards)

def renderOther(data):
    cards = []
    for j in data:
        cards += [showCard(j["name"], j["description"],
                          j["imgurl"], j["web"], j["price"])]
        # test = json.dumps(showCard(place["title"],place["subtitle"]), indent=4)
        # print(test)
    return showCarousel(cards)
