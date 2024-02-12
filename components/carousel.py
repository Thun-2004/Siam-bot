def showCarousel(cards):
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
                                "contents": cards
                        }
                    }
                }
            }
        ]}
    
