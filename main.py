from questions import questions
from keypad import get_answer
from hardware import check_answers

def play_game():
    score = 0
    
    for question in questions:
        print(question["question"])
        
        for choice in question["choices"]:
            print (choice)
            
        answer = get_answer()
        
        if check_answer, question["answer"]):
            score += 1
    print("Final Score:", score, "/", len(questions))
    
play_game()