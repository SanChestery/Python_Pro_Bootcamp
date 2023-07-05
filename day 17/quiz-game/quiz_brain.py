class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self): 
        curr_ques = self.question_list[self.question_number]
        self.question_number += 1
        invalid_input = True
        while invalid_input:
            choice = input(f"Q.{self.question_number}: {curr_ques.text} (True/False)?: ").lower()
            if choice == "true" or choice == "false":
                self.check_answer(choice, curr_ques.answer)
                invalid_input = False
            else:
                print("Invalid input. Please enter True or False!n")

    def check_answer(self, u_answer, corr_answer):
        if u_answer.lower() == corr_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {corr_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")


    def still_has_questions(self):
        return self.question_number < len(self.question_list)
