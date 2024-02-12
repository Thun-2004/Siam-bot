from service.database import getOther
from service.render import renderOther, renderQuickReply


def otherActivity():
    data = ["adult", "child"]
    return renderQuickReply("select type of additional activity: ", data)


def returnotherCard(message):
    data1 = getOther()
    other_type = message["queryResult"]["parameters"]["otherType"]
    selection = []

    for i in data1:
        if other_type == i["type"]:
            selection += [i]

        # print("cards: ", cards)

    return renderOther(selection)
