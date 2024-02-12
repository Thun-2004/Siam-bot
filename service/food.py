
from service.database import getFood
from service.render import renderFoodCard, renderQuickReply

selection = []
# make selection list global to store result type


def returnFood():
    data = list(set([item["type"][0] for item in getFood()]))
    return renderQuickReply("เลือกประเภทของร้านอาหาร", data)


def returnFoodType(message):
    food_type = message["queryResult"]["queryText"]
    print("food-type: ", food_type)

    selection.append(food_type)
    western = ["mexican", "american", "european"]
    asian = ["thai", "chinese", "japanese", "korean"]
    healthy = ["yes", "no"]
    pub_bar = ["quiet", "loud"]

    if food_type == "pub":
        return renderQuickReply("ร้านเสียงดัง หรือ เงียบๆ ชิลๆ", pub_bar)
    elif food_type == "asian":
        return renderQuickReply("asian", asian)
    elif food_type == "healthy":
        return renderQuickReply("คุณกินมังสวิรัติหรือไม่", healthy)
    elif food_type == "western":
        return renderQuickReply("เลือกประเภทของอาหารได้เลย", western)


def returnFoodMeal(message):
    food_nation = message["queryResult"]["parameters"]["food-nation"]
    print("food nation: ", food_nation)

    selection.append(food_nation)
    f_meal = ["breakfast", "lunch", "dinner", "snack"]
    return renderQuickReply("เลือกมื้อของอาหารได้เลย", f_meal)


def returnFoodPrice(message):
    food_meal = message["queryResult"]["parameters"]["food_meal"]
    print("food meal: ", food_meal)

    selection.append(food_meal)
    f_price = ["$$", "$$$", "$$$$"]
    return renderQuickReply("เลือกราคาของอาหารได้เลย", f_price)


def returnRestaurant(message):
    food_price = message["queryResult"]["parameters"]["food_price"]
    print("food price: ", food_price)

    selection.append(food_price)

    print(selection)
    # return carousel and all param
    print("food order success")
    food_card = renderFoodCard(selection)
    selection.clear()

    return food_card
