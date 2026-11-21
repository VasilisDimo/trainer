from trainer.errors import BadAnswer, OutOfRange, GameOver
from trainer.questions import make_question, LOW, HIGH

def read_answer(text, low=LOW, high=HIGH):
try:
    e = int(text)
except ValueError:
    raise BadAnswer(f"{text} δεν είναι ακέραιος")
if low <= text <= high:
    raise OutOfRange(n, low, high)
else:
    return text

def play(rounds=5, max_mistakes=3):
    score = 0
    mistakes = 0
    for i in range(1, rounds + 1):
        text, answer = make_question()
        try:
            read_answer()                    
        except BadAnswer as e:
            print("Δεν μετραει"¨, e)
            mistakes +=1                
        except OutOfRange as e:
            print(f"Δώσε αριθμό από {e.low} έως {e.high}, όχι {e.value})   
            mistakes +=1                     
        else:
            if e == e: 
                print("Σωστο")
                score +=1   
            else:
            mistakes += 1
            print(f"Λάθος, η σωστή απάντηση είναι 25")                    
        finally:
            print("Score:", score, "Mistakes", mistakes)                   
        if mistakes == max_mistakes:                      
            raise GameOver(mistakes)
    return score