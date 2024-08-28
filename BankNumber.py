class BankNumber:
    def __init__(self, real_part, float_part):
        self.real_part = real_part
        self.float_part = float_part

    def __eq__(self, other):
        return (self.real_part == other.real_part) and (self.float_part == other.float_part)

    def __add__(self, other):
        new_real = self.real_part + other.real_part
        new_float = self.float_part + other.float_part
        if new_float >= 100:
            new_real += 1
            new_float -= 100
        return BankNumber(new_real, new_float)

    def __sub__(self, other):
        new_real = self.real_part - other.real_part
        new_float = self.float_part - other.float_part
        if new_float < 0:
            new_real -= 1
            new_float += 100
        return BankNumber(new_real, new_float)

    def __lt__(self, other):
        if self.real_part < other.real_part:
            return True
        elif self.real_part == other.real_part:
            return self.float_part < other.float_part
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return f"{self.real_part}.{self.float_part:02d}"


# Testy pro třídu BankNumber

import unittest

class TestBankNumber(unittest.TestCase):
    
    def test_eq(self):
        bn1 = BankNumber(10, 50)
        bn2 = BankNumber(10, 50)
        bn3 = BankNumber(10, 51)
        self.assertEqual(bn1, bn2)
        self.assertNotEqual(bn1, bn3)

    def test_add(self):
        bn1 = BankNumber(10, 50)
        bn2 = BankNumber(5, 75)
        result = bn1 + bn2
        self.assertEqual(result, BankNumber(16, 25))
        
        bn3 = BankNumber(0, 99)
        bn4 = BankNumber(0, 2)
        result = bn3 + bn4
        self.assertEqual(result, BankNumber(1, 1))

    def test_sub(self):
        bn1 = BankNumber(10, 50)
        bn2 = BankNumber(5, 75)
        result = bn1 - bn2
        self.assertEqual(result, BankNumber(4, 75))

        bn3 = BankNumber(10, 50)
        bn4 = BankNumber(10, 50)
        result = bn3 - bn4
        self.assertEqual(result, BankNumber(0, 0))
        
        bn5 = BankNumber(10, 0)
        bn6 = BankNumber(5, 1)
        result = bn5 - bn6
        self.assertEqual(result, BankNumber(4, 99))

    def test_comparison(self):
        bn1 = BankNumber(10, 50)
        bn2 = BankNumber(5, 75)
        self.assertTrue(bn1 > bn2)
        self.assertTrue(bn2 < bn1)
        self.assertTrue(bn1 >= bn2)
        self.assertTrue(bn2 <= bn1)
        
        bn3 = BankNumber(10, 50)
        bn4 = BankNumber(10, 50)
        self.assertTrue(bn3 >= bn4)
        self.assertTrue(bn3 <= bn4)

    def test_str(self):
        bn1 = BankNumber(10, 5)
        self.assertEqual(str(bn1), "10.05")

        bn2 = BankNumber(0, 0)
        self.assertEqual(str(bn2), "0.00")


if __name__ == "__main__":
    unittest.main()
