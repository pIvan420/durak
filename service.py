import itertools

from model import GameSession


class GameService:
    __card_status = ["Я", "Он", "Неизвестно", "Вышла"]
    __player_move = ["Я", "Он"]
    __move_result = ["Взял", "Отбился"]
    __number = ("Т", "К", "Д", "В", "10", "9", "8", "7", "6", "5", "4", "3", "2")
    __suit = ("Ч", "К", "П", "Б")
    __game = None
    __cur_cards_count = [24, 36, 52]


    # product заменяет вложенные циклы и получаю список из кортежей карт, который итерирую по map
    def __init__(self):
        self.__cards = list(map(lambda x: x[0] + x[1],
                                list(itertools.product(self.__number, self.__suit))))


    def create_game(self, cards_count):
        self.__game = GameSession(self.get_all_cards(cards_count), self.__card_status[2])


    def get_players(self):
        return self.__player_move


    def get_move_result(self):
        return self.__move_result


    def get_suit(self):
        return self.__suit


    def get_all_cards(self, count):
        return self.__cards[:count]


    def get_your_cards(self):
        return self.__game.get_cards(self.__card_status[0])


    def get_enemy_cards(self):
        return self.__game.get_cards(self.__card_status[1])

    def get_unknown_cards(self):
        return self.__game.get_cards(self.__card_status[2])

    def get_out_cards(self):
        return self.__game.get_cards(self.__card_status[3])

    def get_cur_cards_count(self):
        return self.__cur_cards_count

    def add_enemy_cards(self, arr):
        self.__game.change_cards_status(arr, self.__card_status[1])

    def take_cards(self, arr):
        self.__game.change_cards_status(arr, self.__card_status[0])


    def is_unknown_cards(self, arr):
        unknown_cards = self.__game.get_cards(self.__card_status[2])
        # Если длина set суммы массивов равна длине set только массива неизвестных, то в arr все карты неизвестны
        if len(set(unknown_cards + arr)) == len(set(unknown_cards)):
            return True
        else:
            return False


    def is_not_out_cards(self, arr):
        not_out_cards = self.__game.get_cards(self.__card_status[0],
                                              self.__card_status[1],
                                              self.__card_status[2])
        if len(set(not_out_cards + arr)) == len(set(not_out_cards)):
            return True
        else:
            return False



    def change_game(self, player_move, move_result, cards_on_table):
        if move_result == self.__move_result[1]:
            self.__game.change_cards_status(cards_on_table, self.__card_status[3])
        elif move_result == self.__move_result[0]:
            if player_move == self.__player_move[0]:
                self.__game.change_cards_status(cards_on_table, self.__card_status[0])
            elif player_move == self.__player_move[1]:
                self.__game.change_cards_status(cards_on_table, self.__card_status[1])
