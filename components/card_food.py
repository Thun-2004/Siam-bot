def showcardFood(name, location, imgUri, postback):
    # name, location, imgUri, location
    return {
        "type": "bubble",
        "size": "mega",
        "direction": "ltr",
        "hero": {
            "type": "image",
            "url": imgUri,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": postback
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": name,
                    "weight": "bold",
                    "size": "xl",
                    "wrap": True
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": location,
                            "size": "md",
                            "color": "#999999",
                            "margin": "lg",
                            "wrap": True
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "WEBSITE",
                        "uri": postback
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "margin": "sm"
                }
            ]
        }
    }
