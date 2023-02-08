from nbresult import ChallengeResultTestCase


class TestOptimal_k(ChallengeResultTestCase):
    def test_optimal_K_around_10(self):
        self.assertGreaterEqual(self.result.optimal_k, 5)
        self.assertLessEqual(self.result.optimal_k, 14)
