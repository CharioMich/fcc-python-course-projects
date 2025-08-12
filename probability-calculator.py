import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for balls in kwargs:
            for i in range(kwargs[balls]):
                self.contents.append(balls)


    def draw(self, number):
        if number >= len(self.contents):
            drawn = copy.copy(self.contents)
            self.contents.clear()
        else:
            drawn = random.sample(self.contents, k=number)
            for ball in drawn:
                self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        counter = 0
        obj = copy.deepcopy(hat)
        drawn = obj.draw(num_balls_drawn)
        for j in expected_balls:
            if drawn.count(j) >= expected_balls[j]:
                counter += 1
        if counter == len(expected_balls):
            M += 1
    propability = M / num_experiments
    return propability