import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
        self.distan = 90

    @classmethod
    def tearDownClass(cls):
        results_ = {}
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                results_.update({key: value.name})
            print(results_)

    def test_tourne1(self):
        tourne_1 = Tournament(self.distan, self.runner_1, self.runner_3)
        result = tourne_1.start()
        self.all_results['test_tourne1'] = result

    def test_tourne2(self):
        tourne_2 = Tournament(self.distan, self.runner_2, self.runner_3)
        result = tourne_2.start()
        self.all_results['test_tourne2'] = result

    def test_tourne3(self):
        tourne_3 = Tournament(self.distan, self.runner_1, self.runner_2, self.runner_3)
        result = tourne_3.start()
        self.all_results['test_tourne3'] = result