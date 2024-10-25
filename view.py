from controller import GameController
import os

controller = GameController()

def game_process():
    for i in controller.get_suit():
        one_suit = []
        for j in controller.get_unknown_cards():
            if j[-1] == i: one_suit.append(j)
        print(" ".join(one_suit))
    print("#" * 25)
    print("Известные карты противника: " + " ".join(controller.get_enemy_cards()))
    print()
    print("Ваши карты: " + " ".join(controller.get_your_cards()))


print("Пример для ввода карт: 6 черви = 6Ч, дама крести = ДК, 2 пики = 2П, валет буби = ВБ")

flag0 = True
while flag0:
    cards_count = int(input("Введите кол-во карт: "))

    try:
        controller.game_registration(cards_count)
        flag0 = not flag0
    except Exception as e:
        print(e)

    os.system('cls')

while len(controller.get_unknown_cards()) > 0:

    flag1 = True
    if len(controller.get_your_cards()) >= 6: flag1 = False

    while flag1:
        try:
            your_cards = str(input("Введите взятые из колоды карты (через пробел): ")).split(" ") #todo могу сделать, что карты беру только unknown
            controller.take_unknown_cards(your_cards)
            flag1 = not flag1
        except Exception as e:
            os.system('cls')
            print(e)


    os.system('cls')


    flag2 = True
    while flag2:
        game_process()
        try:
            player_move = input("Кто отбивается (Я, Он)? Ответ: ")
            cards_on_table = input("Какие карты на столе? Ответ (через пробел): ").split(" ") #todo могу сделать, что вышедшие карты не беру
            move_result = input("Взял или Отбился? Ответ: ")

            controller.set_game_round_result(player_move, move_result, cards_on_table)
            flag2 = not flag2
        except Exception as e:
            os.system('cls')
            print(e)


os.system('cls')
game_process()
