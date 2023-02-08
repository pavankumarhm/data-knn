from nbresult import ChallengeResultTestCase


class TestBest_model(ChallengeResultTestCase):
    def test_best_model(self):
        self.assertEqual(self.result.model, "KNN")
