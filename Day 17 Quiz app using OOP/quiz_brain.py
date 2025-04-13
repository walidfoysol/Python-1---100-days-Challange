

class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        
    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> int:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(current_question.answer, answer)

    def check_answer(self,correct_answer, answer):
        if answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
