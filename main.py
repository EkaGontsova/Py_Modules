import datetime
from application.salary import Salary
from application.db.people import get_employees


if __name__ == '__main__':
    print("Current date:", datetime.datetime.now())

    amount = float(input("Enter salary amount: "))
    emp_salary = Salary(amount)
    tax = emp_salary.calculate_tax()
    bonus = emp_salary.calculate_bonus()
    total = emp_salary.calculate_salary()

    print(f"Tax amount: {tax}")
    print(f"Bonus amount: {bonus}")
    print(f"Total salary: {total}")

    employees_list = get_employees()
    for employee in employees_list:
        print(employee)
