from nbresult import ChallengeResultTestCase


class TestScale_sensitivity(ChallengeResultTestCase):
    def test_rescaled_features(self):
        self.assertEqual(self.result.rescaled_features.min().all(), 0)

    def test_score_inscrease(self):
        self.assertGreater(self.result.rescaled_score, self.result.base_score)
