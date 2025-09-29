class Quiz:
    def __init__(self):
        self.scores = 0

    def ask_answer(self, question, answers):
        
        answer_number = 1
        print(question)

        for answer in answers:
            print(f"{answer_number}. {answer}")
            answer_number += 1
        return input("\nAnswer: ")

    def check_answer(self, given_answer, correct_answer):
        # Checking the answer
        if given_answer == correct_answer:
            self.scores += 20
            return "Hooray! That's Correct 😊... \n"
        else:
            return "No! That's not Correct 😑... \n"

    def show_result(self):
        if 20 < self.scores <= 60:
            print(f"\nScore: {self.scores} \nGrade: Pass (S)")
        else:
            print(f" \nScore: {self.scores} Faild")
            