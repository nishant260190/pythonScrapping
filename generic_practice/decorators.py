# ********* CLOSURE ********

# # ********* first try ********

# # Here below inner function is returned not called 
# # that's why we have to save that in x variable and than call.

# def outer_function():
# 	message = 'hi'
# 	def inner_function():
# 		print(message)
# 	return inner_function


# x = outer_function()
# x()

# # *****************

# # Here below plz check return line of outer function here we are calling function.
# def outer_function():
# 	message = 'hi'
# 	def inner_function():
# 		print(message)
# 	return inner_function()


# outer_function()

# *************************


# def outer_function(msg):
# 	def inner_function():
# 		print(msg)
# 	return inner_function


# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# *************************

# ********* DECORATOR ********

# first try 

# def decorator_function(original_function):
# 	def wrapper_function(*args, **kwargs):
# 		print("wrapper executed this before {}".format(original_function.__name__))
# 		return original_function(*args, **kwargs)
# 	return wrapper_function

# @decorator_function
# def display():
# 	print("display func run")

# @decorator_function
# def display_info(name, age):
# 	print("display_info ran with arguments ({}, {})".format(name, age))

# display_info('John', 25)

# # decorated_display = decorator_function(display)
# # decorated_display()

# # display()

# *********************

# ***************** second try ***********

# class decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print("call method executed this before {}".format(self.original_function.__name__))
# 		return self.original_function(*args, **kwargs)

# @decorator_class
# def display():
# 	print("display func run")

# @decorator_class
# def display_info(name, age):
# 	print("display_info ran with arguments ({}, {})".format(name, age))

# display_info('John', 25)
# display()

# *********************

# ***************** third try ***********

from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in : {} sec'.format(orig_func.__name__, t2))
		return result
	return wrapper

# @decorator_class
# def display():
# 	print("display func run")


import time

@my_timer
@my_logger
def display_info(name, age):
	time.sleep(1)
	print("display_info ran with arguments ({}, {})".format(name, age))


display_info('Nishant', 28)
