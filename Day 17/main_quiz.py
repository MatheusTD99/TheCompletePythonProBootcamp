from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

class Question_number:
    def __init__(self, q_number, q_list):
        self.q_number = q_number = 0
        self.q_list = q_list


question_bank = []
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

