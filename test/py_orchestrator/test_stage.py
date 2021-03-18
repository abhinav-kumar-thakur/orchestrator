from py_orchestrator.stage import Stage


class Adder(Stage):
    def perform(self, state):
        return self.configs['a'] + self.configs['b']


class TestStage:
    def test_run(self):
        configs = {'a': 1, 'b': 2}
        assert Adder(configs).perform(None) == 3
