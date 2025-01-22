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
