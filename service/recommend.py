from components.carousel import showCarousel
from service.database import getData, searchByType
from service.render import renderCard, renderQuickReply


def recommendLocation(message):
    # print(json.dumps(message, indent=4 ,ensure_ascii=False))
    place_type = message["queryResult"]["parameters"]["place_type"]
    print("place_type", place_type)
    cards = []
    # add condition
    if 'บันเทิง' in place_type:
        cards += renderCard(searchByType('entertain'))

    if "ศิลปะ" in place_type:
        cards += renderCard(searchByType('exhibition'))

    if "shopping" in place_type:
        cards += renderCard(searchByType('shopping'))
    if "minimal" in place_type:
        cards += renderCard(searchByType('minimal'))
    if "ทางสายกลาง" in place_type:
        cards += renderCard(searchByType('religion'))

    return showCarousel(cards)


def recommendQuick():
    data = getData()
    return renderQuickReply("กรอกประเภทของที่เที่ยว", data)
