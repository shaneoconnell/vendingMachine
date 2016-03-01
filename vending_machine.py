class TestVendingMachine(unittest.TestCase):
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    denominations.sort(reverse=True)
    def give_change(self, amount, change):
        if amount == 0:
            return change
        else:
            for denom in self.denominations:
                if amount >= denom:
                    change.append(denom)
                    amount -= denom
                    return self.give_change(amount, change)
    def test_no_change(self):
        coins = self.give_change(0, [])
        self.assertEqual(coins, [])
    def test_return_some_change(self):
        coins = self.give_change(4, [])
        self.assertEqual(coins, [2,2])