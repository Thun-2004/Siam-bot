def replyFood(data, food_type, food_nation, meal, price):
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "text",
                        "text": "ผลการค้นหา\n" + data + "\n" + food_type + "\n" + food_nation + "\n" + meal + "\n" + price,
                        
                    }
                }
            }
        ]}


def test():
    return replyFood("food", "western", "us", "lunch", "$$$")