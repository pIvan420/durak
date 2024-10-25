class GameSession:

    def __init__(self, cards, status):
        self.__cards = list(map(lambda x: Card(x, status), cards))


    def change_cards_status(self, arr, status):
        for i in arr:
            for j in self.__cards:
                if j.get_name() == i:
                    j.set_status(status)
                    break


    def get_cards(self, *status):
        return list(map(lambda x: x.get_name(), filter(lambda x: x.get_status() in status, self.__cards)))


class Card:
    __status = ""

    def __init__(self, name, status):
        self.__name = name
        self.__status = status


    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status