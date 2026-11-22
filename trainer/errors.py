import math, random



class TrainerError(Exception):
    pass

class BadAnswer(TrainerError):
    def __init__(self, e):
        if isinstance(e, int):
            pass

class OutOfRange(TrainerError):
    def __init__(self, value, low, high):
        self.value = value   
        self.low = low
        self.high = high 
        super().__init__(f"{value} είναι εκτός ορίων {[low, high]}")
                                   

    
class GameOver(TrainerError):
    def __init__(self, mistakes):
        self.mistakes = mistakes
        super().__init__(f"Τέλος παιχνιδιού: {mistakes} λάθη")
        


