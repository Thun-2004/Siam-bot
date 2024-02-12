from service.database import getHotel
from service.render import renderAccom, renderQuickReply

selection = []


def accomType():
    # accom_type = [hotel['type'] for hotel in getHotel()]
    accom_type = ["hostel", "hotel", "condo"]
    return renderQuickReply("เลือกประเภทของที่พัก", accom_type)


def accomPrice(message):
    type = message["queryResult"]["parameters"]["accomType"]
    selection.append(type)
    accom_price = ["฿฿฿฿", "฿฿฿฿฿", "฿฿฿฿฿฿"]
    print("accome-type", type)
    return renderQuickReply("เลือกราคาของที่พัก", accom_price)


def returnAccom(message):
    price = message["queryResult"]["parameters"]["accomPrice"]
    selection.append(price)
    print("accom-price", price)
    print("ผู้ใช้เลือก >>>>", selection)
    final = renderAccom(selection)
    selection.clear()
    return final
