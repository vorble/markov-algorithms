# markov.py
#
# Utilities for running Markov algorithms.

import sys
import time

class MarkovAlgorithm(object):
    def __init__(self, rules):
        self._rules = rules

    def _findNextRule(self, data):
        for (match, replace) in self._rules:
            index = data.find(match)
            if index >= 0:
                return (match, index, replace)
        return None, None, None

    def start(self, data):
        return MarkovAlgorithmRun(self, data)

class MarkovAlgorithmRun(object):
    def __init__(self, alg, data):
        self._alg = alg
        self.data = data

    def step(self):
        match, index, replace = self._alg._findNextRule(self.data)
        if match is None:
            return False
        self.data = self.data[:index] + replace + self.data[index + len(match):]
        return True

    def finish(self):
        while self.step():
            pass
        return self.data

def run(rules, data):
    return MarkovAlgorithm(rules).start(data).finish()

def show(rules, data):
    result = MarkovAlgorithm(rules).start(data)
    while True:
        print(result.data)
        if not result.step():
            break
    return result.data

def animate(rules, data):
    result = MarkovAlgorithm(rules).start(data)
    last_data = ''
    while True:
        # This will probably mess up when the terminal is too narrow.
        sys.stdout.write('\x0d' + ' ' * len(last_data))
        sys.stdout.write('\x0d' + result.data)
        last_data = result.data
        time.sleep(0.25)
        if not result.step():
            break
    print()
    return result.data

