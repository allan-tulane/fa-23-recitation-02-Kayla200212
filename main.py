"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		print(n, a, b)
		return a * 1 + n
  	#otherwise
	else:
		print(n, a, b)
		new_n = n // b
		new_w = a * simple_work_calc(new_n, a, b) + n
	return new_w

print("result", simple_work_calc(10,2,2))

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n==1:
		print(n,a,b)
		return a * 1 + n
	else:
		print(n,a,b)
		new_n = n // b
		new_w = a * work_calc(new_n, a, b) + simple_work_calc
		return new_w

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
	print(res)

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for
	given input sizes.
	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
		n,
		span_fn1,
		span_fn2
		))
	return result
def test_compare_span():
	# TODO
	pass