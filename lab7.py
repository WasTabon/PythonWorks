import random

class MagicBall:
    def __init__(self):
        self.answers = ["Yep", "Nope", "Maybe"]

    def charivna_kulka(self, question):
        if not isinstance(question, str):
            raise ValueError('Enter another type of value')

        if len(question) == 0:
            raise ValueError('Question shouldn\'t be an empty value')

        return f'{question}: {random.choice(self.answers)}'

    def configure_magic_ball(self, new_answers: list):
        for new_answer in new_answers:
            position = random.randint(0, len(self.answers))
            self.answers.insert(position, new_answer)

magic_ball = MagicBall()
magic_ball.configure_magic_ball(["Of course", "To be or not to be", "I have no idea"])
print(magic_ball.charivna_kulka("Will be sunny today?"))