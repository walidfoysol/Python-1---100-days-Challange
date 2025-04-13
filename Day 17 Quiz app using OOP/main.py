from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
points = 0

for element in question_data:
    question_bank.append(Question(element["text"], element["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_questions():
    quiz_brain.next_question()

print(f"You have completed the quiz!\nYour final Score is {quiz_brain.score}/{quiz_brain.question_number}")
