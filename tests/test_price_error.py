from nbresult import ChallengeResultTestCase


class TestPrice_error(ChallengeResultTestCase):
    def test_price_error_range(self):
        self.assertTrue(25000 < abs(self.result.error) < 35000)
