class Game(object):

    _board = list(range(1,10))

    def create_field(self,_board):
        print(" ")
        for i in range(3) :
            print("|", _board[0+i*3] ,"|", _board[1+i*3], "|", _board[2+i*3], "|")
            print(" ")

    def consume_data(self, input_symbol):
        valid = False
        while not valid:
            choise = input("Введите координаты ячейки для вставки символа " + input_symbol + " ")
            try:
                choise = int(choise)
            except ValueError:
                print("Некорректные координаты,попробуйте еще раз")
                continue  
            if choise >= 1 and choise <= 9:
                if(str(self._board[choise-1]) not in "xo"):
                    self._board[choise-1] = input_symbol
                    valid = True
                else:
                    print("Ячейка занята")
            else:
                print("Некорректные координаты,должны быть от 1 до 9")   

    def check_board_state(self,_board):
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for elem in win_coord:
            if ( _board[elem[0]] == _board[elem[1]] == _board[elem[2]] ):
                return _board[elem[0]]
        return False 

    def main(self):
        counter = 0
        win = False
        while not win:
            self.create_field(self._board)
            if counter % 2 == 0:
                self.consume_data("x")
            else:
                self.consume_data("o")
            counter += 1
            if (counter > 4) & (counter < 9):
                if self.check_board_state(self._board) != False:
                    print('Игрок  {} победил'.format(str(counter % 2)))
                    # print("Игрок " + str(counter % 2) + " победил")
                    win = True
                    break        
            if counter == 9:
                print("Ничья")
                break
        self.create_field(self._board)    

# game = Game()
# game.main()