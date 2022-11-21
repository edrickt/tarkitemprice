import requests

class TarkovMarket:
    def __init__(self, token):
        self.token = token

    def get_data(self, url):
        response = requests.get(url).json()
        if not response:
            raise self.InvalidItem
        elif "Access denied" in str(response):
            raise self.InvalidAPIKey
        else:
            return response

    def get_item_by_name(self, item_name):
        return Item(self.get_data(f"https://tarkov-market.com/api/v1/item?q={item_name}&x-api-key={self.token}"))

    def get_all_items(self):
        return self.get_data(f"https://tarkov-market.com/api/v1/items/all?x-api-key={self.token}")

class Item:
    def __init__(self, data):
        self.__data = data[0]
        self.uid = self.__data["uid"]
        self.tags = self.__data["tags"]
        self.name = self.__data["name"]
        self.short_name = self.__data["shortName"]
        self.price = self.__data["price"]
        self.base_price = self.__data["basePrice"]
        self.avg_24h_price = self.__data["avg24hPrice"]
        self.avg_7d_price = self.__data["avg7daysPrice"]
        self.trader_name = self.__data["traderName"]
        self.trader_price = self.__data["traderPrice"]
        self.trader_price_currency = self.__data["traderPriceCur"]
        self.updated = self.__data["updated"]
        self.slots = self.__data["slots"]
        self.diff_24h = self.__data["diff24h"]
        self.diff_7d = self.__data["diff7days"]
        self.icon = self.__data["icon"]
        self.link = self.__data["link"]
        self.wiki_link = self.__data["wikiLink"]
        self.img = self.__data["img"]
        self.img_big = self.__data["imgBig"]
        self.bsg_id = self.__data["bsgId"]
        self.is_functional = self.__data["isFunctional"]
        self.reference = self.__data["reference"]
        