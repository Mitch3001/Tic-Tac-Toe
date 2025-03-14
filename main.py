#колличество клеток
board_size = 3
#игровое поле
board = [1,2,3,4,5,6,7,8,9]

MODE_HUMAN_VS_HUMAN = '1'

MODE_HUMAN_VS_AI = '2'
def draw_board():
    '''Выводим игровое поле'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('',board[i*3], '|', board[1 + i*3], '|', board[2+ i*3], '|')
        print(('_' * 3 + '|')*3)
def game_step(index, char):
    '''Выполняем ход'''
    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False

    board[index - 1] = char
    return True
    pass

def check_win(board):
    ''' Проверяем победу одного из игроков '''
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (6,7,8), # Горизонтальные линии
        (0,3,6), (1,4,7), (2,5,8), # Вертикальные линии
        (0,4,8), (2,4,6) #Диаганальные линии
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def computer_step(human, ai):
    '''Простой ИИ для игры с человеком'''

    # найти доступные шаги
    available_steps = [i-1 for i in board if type(i) == int]

    # успешные шаги в порядке приоритетности
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    win_steps1 = (0, 2, 4, 6, 8, 1, 3, 5, 7)
    win_steps2 = (2, 4, 6, 8, 1, 3, 5, 7, 0)
    win_steps3 = (4, 6, 8, 1, 3, 5, 7, 0, 2)


    for char in (ai, human):
      for pos in available_steps:
        #клонирование игровой доски
        board_ai = board [:]
        board_ai[pos] = char
        if (check_win(board_ai) != False):
            return pos

    # Если мы тут, то не нашли вариант для выигрыша
    for pos in win_steps:
        if (pos, available_steps):
            return pos



    return False

def next_player(curret_player):
    ''' определяем чей следующий ход'''
    if (curret_player == 'X'):
        return 'O'

    return 'X'

def start_game(mode):
    #текущий игрок
    curret_player = 'X'
    ai_player = 'O'
    #номер шага
    step = 1
    draw_board()
    while (step < 10) and (check_win(board) == False):
        index = input('Ходит игрок' + ' ' + curret_player + ' ' + 'Введите номер поля (0 - выход):')

        if (int(index) == '0'):
            break

        # Если получилось сделать шаг
        if (game_step(int(index), curret_player)):
         print('Удачный ход')

         curret_player = next_player(curret_player)

        #Увеличим номер хода
        step += 1

        if (mode == MODE_HUMAN_VS_AI):
            ai_step = computer_step('X', 'O')
            # если компьютер нашел куда ходить
            if (type(ai_step) == int):
                # ходит компьютер
                board[ai_step] = ai_player
                curret_player = next_player(curret_player)
                step += 1

        draw_board()
    else:
        print('Неверный номер! Повторите!')

    if (step == 10):
        print('Игра окончена! Ничья!')
    elif check_win() != False:
        print('Выиграл ' + check_win(board))

    print('Выиграл ' + check_win(board))



print('Добро пожаловать в крестики-нолики!')

mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input("Режим игры: \n1 - Человек против Человека\n2 - Человек против Компьютер\nВыбери режим игры:)")

start_game(mode)