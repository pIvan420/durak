from service import GameService


class GameController:
    __gameService = GameService()


    def game_registration(self, cards_count):
        try:
            self.reg_validation(cards_count)
        except Exception as e:
            raise Exception(e)

        self.__gameService.create_game(cards_count)


    def get_suit(self):
        return self.__gameService.get_suit()


    def get_your_cards(self):
        return self.__gameService.get_your_cards()


    def get_enemy_cards(self):
        return self.__gameService.get_enemy_cards()


    def get_unknown_cards(self):
        return self.__gameService.get_unknown_cards()


    def get_out_cards(self):
        return self.__gameService.get_out_cards()


    def take_unknown_cards(self, arr):
        try:
            self.take_unknown_cards_validator(arr)
        except Exception as e:
            raise Exception(e)
        self.__gameService.take_cards(arr)
        if len(self.get_unknown_cards() + self.get_enemy_cards()) <= 6:
            self.__gameService.add_enemy_cards(self.get_unknown_cards())



    def set_game_round_result(self, player_move, move_result, cards_on_table):
        try:
            self.game_round_result_validator(player_move, move_result, cards_on_table)
        except Exception as e:
            raise Exception(e)
        self.__gameService.change_game(player_move, move_result, cards_on_table)


    #Валидаторы

    def game_round_result_validator(self, player_move, move_result, cards_on_table):
        if player_move not in self.__gameService.get_players(): raise Exception("Некорректные данные! Неясно, кто отбивается")
        if move_result not in self.__gameService.get_move_result(): raise Exception("Некорректные данные! Неясен исход раунда")
        if len(cards_on_table) != len(set(cards_on_table)):
            raise Exception("Некорректные данные! Карты не могут повторяться")
        if self.__gameService.is_not_out_cards(cards_on_table) is False:
            raise Exception("Некорректные данные! Повторите ввод карт на столе")



    def reg_validation(self, cards_count):
        cur_cards_count = self.__gameService.get_cur_cards_count()
        if cards_count not in cur_cards_count:
            raise Exception(f"Некорректные данные! Кол-во карт может составлять: {", ".join(cur_cards_count)}")


    def take_unknown_cards_validator(self, arr):
        if self.__gameService.is_unknown_cards(arr) is False:
            raise Exception("Некорректные данные! Повторите ввод взятых карт")
        arr.extend(self.__gameService.get_your_cards())
        if len(arr) != len(set(arr)): raise Exception("Некорректные данные! Карты не могут повторяться")
        if len(arr) > 6: raise Exception("Некорректные данные! На руках не может быть больше 6 карт")