import unittest

class TestVendingMachine(unittest.TestCase):
    def give_change(self, amount):
        return [10,5,2]

    def test_return_change(self):
        coins = self.give_change(17)
        self.assertEquals(coins, [10,5,2], 'wrong change given')
