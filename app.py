import os
from flask import make_response, request, Flask
from components.testcard import renderTestCard, testCard
from service.location import locationService
from service.other import otherActivity, returnotherCard
from service.recommend import recommendLocation, recommendQuick
from components.image import testimage
import json
from service.search import responseSearch
from service.food import returnFood, returnFoodMeal, returnFoodPrice, returnFoodType, returnRestaurant
from components.foodmessage import test
from service.hotel import accomType, accomPrice, returnAccom
from service.testAccomcard import testaccomCard
# Flask
app = Flask(__name__)

# การบอกว่าใช้ path นี้ในการส่ง
# MainFunction


@app.route('/siam', methods=['POST'])
def MainFunction():
    # รับ message จาก dialogflow
    rawMessage = request.get_json(silent=True, force=True)
    # ส่ง message ไปให้ generating_answer ทำการสร้างคำตอบ
    bot_respone = generating_answer(rawMessage)
    r = make_response(bot_respone)
    # make_response = return bot_response
    r.headers['Content-Type'] = 'application/json'
    return r


def generating_answer(message):
    # print(json.dumps(message, indent=4 ,ensure_ascii=False))
    intentName = message["queryResult"]["intent"]["displayName"]
    print("intent group: ", intentName)

    # existing intent group
    simple_dict = {
        'imgTest': testimage,
        'place_recommend': recommendQuick,
        'food': returnFood,
        'render-food': test,
        'card': renderTestCard,
        'accom': accomType,
        'testAccom': testaccomCard,
        'others': otherActivity
    }
    # tough_dict = {
    #     'searchName': responseSearch,
    #     'recommend': recommendLocation,
    #     'searchByName': responseSearch,
    #     'location': locationService,
    #     'food-type': returnFoodType,
    #     'food-nation': returnFoodMeal,
    #     'food-meal': returnFoodPrice,
    #     'food-price': returnRestaurant,
    #     'accom-type': accomPrice,
    #     'accom-price': returnAccom,
    #     'others-type': returnotherCard
    # }

    # food price return carousel and all param
    if intentName in simple_dict:
        answer = simple_dict[intentName]()
    # elif intentName in tough_dict:
    #     answer = tough_dict[intentName](message)
    else:
        answer = {"fulfillmentText": "พิมพ์อีกครั้งได้มั้ย"}

    # print(answer)
    botResponse = json.dumps(answer, indent=4)
    # cvt dict to json for APi
    # print(botResponse)
    return botResponse


@app.route('/', methods=['GET'])
def test():
    return os.getenv('DB_URI')


# กำหนด port ให้ flask
if __name__ == '__main__':
    app.run(threaded=True, port=5050)

