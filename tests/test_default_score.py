from nbresult import ChallengeResultTestCase


class TestDefault_score(ChallengeResultTestCase):
    def test_score(self):
        self.assertGreater(self.result.score, 0.55)
