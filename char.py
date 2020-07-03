class player_char():
    def __init__(self):
        self.hp = 100
        self.mp = 100


    def move_right(self):
        #카드 선택하면 앞으로 움직임
        print('right')
    def move_left(self):
        #카드 선택하면 뒤로 움직임
        print('left')
    def move_up(self):
        # 카드 선택하면 위로 움직임
        print('up')
    def move_down(self):
        # 카드 선택하면 아래로 움직임
        print('down')

    def att_side(self):
        # 양 옆으로 공격, 공격력: 50, 마나: 50
        print('side att!')
    def att_cross(self):
        # 위 아래 크로스로 공격, 공격력: 35, 마나: 25
        print('cross att!')
    def att_circle(self):
        # 주위를 다 공격, 공격력: 20, 마나: 15
        print('circle att!')

class computer_char():
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.comX = 640
        self.comY = 280

    def move_right(self):
        # 카드 선택하면 앞으로 움직임
        print('right')
    def move_left(self):
        # 카드 선택하면 뒤로 움직임
        print('left')
    def move_up(self):
        # 카드 선택하면 위로 움직임
        print('up')
    def move_down(self):
        # 카드 선택하면 아래로 움직임
        print('down')

    def att_side(self):
        # 양 옆으로 공격, 공격력: 50, 마나: 50
        print('side att!')
    def att_cross(self):
        # 위 아래 크로스로 공격, 공격력: 35, 마나: 25
        print('cross att!')
    def att_circle(self):
        # 주위를 다 공격, 공격력: 20, 마나: 15
        print('circle att!')
