from random import choice

class Robot(object):
    
    letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    numbers = [chr(x) for x in range(ord('0'), ord('9') + 1)]
    names = set()

    @staticmethod
    def create_name():
        is_different = False
        while not is_different:
            candidate = choice(Robot.letters) + choice(Robot.letters) + \
                choice(Robot.numbers) + choice(Robot.numbers) + choice(Robot.numbers)
            if not candidate in Robot.names:
               is_different = True
        return candidate
       
    def __init__(self):
        self.name = Robot.create_name()
        Robot.names.add(self.name)

    def reset(self):
        self.name = Robot.create_name()
        Robot.names.add(self.name)
