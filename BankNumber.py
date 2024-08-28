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
