import copy
from dlgo.gotypes import Player

class Move(): #수 설정 : 돌 놓기, 차례 넘기기, 대국 포기
    def  __init__(self, point=None, is_pass=False, is_resign=False): #기사가 자기 차례에 할 수 있는 행동(is_play, is_pass, is_resign)을 설정
        assert (point is not None) ^ is_pass ^ is_resign # (== 중간 or (is_pass is True) or (is_resign is True))
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        return Move(point=point)
    
    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)
    
    @classmethod
    def resign(cls):
        return Move(is_resign=True)
    



class GoString(): #이음을 set으로 인코딩
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)

    def merged_with(self, go_string): #양 선수의 이음의 모든 돌을 저장한 새 이음을 반환한다 ( 두 개의 그룹을 연결한 경우 merged_with()메소드 호출 )
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones
        )
    
    @property
    def num_liberties(self):
        return len(self.liberties)
    def __eq__(self, other):
        return isinstance(other, GoString) and \
        self.color == other.color and \
        self.stones == other.stones and \
        self.liberties == other.liberties
    