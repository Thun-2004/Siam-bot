def showcardAccom(name, imgurl, web, price, location):
    return {
        "type": "bubble",
        "size": "mega",
        "direction": "ltr",
        "hero": {
            "type": "image",
            "url": imgurl,
            "size": "full",
            "aspectRatio": "20:11",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": web
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
                    "size": "xxl",
                    "color": "#696969",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": "Price: " + price,
                    "size": "md",
                    "color": "#808080",
                    "margin": "lg",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": "Location: " + location,
                    "size": "md",
                    "color": "#808080",
                    "margin": "lg",
                    "wrap": True
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
                        "uri": web
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
