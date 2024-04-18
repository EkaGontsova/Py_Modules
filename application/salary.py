class Salary:
    def __init__(self, amount):
        self.amount = amount

    def calculate_salary(self):
        tax_amount = self.calculate_tax()
        bonus_amount = self.calculate_bonus()
        total = self.amount - tax_amount + bonus_amount
        return total

    def calculate_tax(self):
        tax_rate = 0.13
        tax_amount = self.amount * tax_rate
        return tax_amount

    def calculate_bonus(self):
        bonus_rate = 0.1
        bonus_amount = self.amount * bonus_rate
        return bonus_amount
