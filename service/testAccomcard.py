from components.card_hotel import showcardAccom


def testaccomCard():
    print("test-accom success")
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "flex",
                                "altText": "This is a Flex Message",
                                # bring JSON payload here
                                "contents": showcardAccom("abc", "https://cdn.discordapp.com/attachments/972401382193778701/983347217886748672/unknown.png", "https://www.novotelbkk.com/th/", "123445", "999/99 โรงแรมเซ็นทาราแกรนด์ฯ เซ็นทรัลเวิลด์ ถนน พระรามที่ ๑ แขวง ปทุมวัน เขตปทุมวัน กรุงเทพมหานคร 10330")
                    }
                }
            }
        ]}
