import random
from typing import List


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        n = len(words)
        while n > 0:
            guess = random.choice(words)
            matches = master.guess(guess)
            if matches == 6:
                return
            words = [w for w in words if match(w, guess) == matches]
            n -= 1
