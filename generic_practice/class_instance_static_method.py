class Employee:
	num_of_emps = 0
	raise_amt = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@email.com"
		self.pay = pay

		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)

	# def apply_raise(self, a):
	# 	print("check that overloading does not exists in python")

	@classmethod
	def set_raise_amt(cls, amount):
		# pass
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split("-")
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False

		return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.raise_amt)
print(emp_1.pay)
print(emp_2.pay)

emp_1.apply_raise()

print(emp_1.pay)
print(emp_2.pay)

Employee.set_raise_amt(2)
emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)

new_emp_1 = Employee.from_string("John-Doe-70000")
print(new_emp_1.pay)

import datetime

my_Date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_Date))