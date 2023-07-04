from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system

system('cls')

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")