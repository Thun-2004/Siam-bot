


def quickReply(description, items):
    print("quickReply success")
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "text",
                        "text": description,
                        "quickReply": {
                            "items": items
                        }
                    }
                }
            }
        ]}
   
    
    
