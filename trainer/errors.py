import math, random


class TrainerError(Exception):
    pass

class BadAnswer(TrainerError):
    pass

class OutOfRange(TrainerError):
    def __init__(self, value, low, high):
        super().__init__(f"{value} είναι εκτός ορίων {[low, high]}")
        self.value = value   
        self.low = low
        self.high = high                                    

    
class GameOver(TrainerError):
    def __init__(self, mistakes):
        super().__init__(f"Τέλος παιχνιδιού: {mistakes} λάθη και {self.mistakes}")
        self.mistakes = mistakes


