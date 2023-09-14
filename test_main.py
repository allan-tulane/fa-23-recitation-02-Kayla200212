from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 52
	assert work_calc(20, 3, 2) == 473
	assert work_calc(30, 4, 2) == 1808

	assert work_calc(8, 2, 2) == 48
	assert work_calc(9, 3, 2) == 147
	assert work_calc(15, 3, 2) == 171

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 31
	assert work_calc(20, 1, 2, lambda n: n*n) == 401
	assert work_calc(30, 3, 2, lambda n: n) == 573

	assert work_calc(8, 2, 2, lambda n: n) == 48
	assert work_calc(9, 3, 2, lambda n: 1) == 121
	assert work_calc(15, 2, 2, lambda n: 1) == 31

def curry_span(a, b, f):
	return lambda n: span_calc(n, a, b, f)
def curry_work_calc(a, b, f):
	return lambda n: work_calc(n, a, b, f)

def test_compare_span():
	assert span_calc(10, 2, 2, lambda n: 1) == 4
	assert span_calc(20, 1, 4, lambda n: n*n) == 426
	assert span_calc(30, 3, 4, lambda n: n) == 38
	
	span_fn1 = curry_span(2, 2, lambda n:1)
	span_fn2 = curry_span(2, 2, lambda n: n**2)
	res = compare_span(span_fn1, span_fn2)
	print_results(res)

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	work_fn1 = curry_work_calc(3, 2, lambda n:1)
	# create work_fn2
	work_fn2 = curry_work_calc(4, 2, lambda n:n**2)
	res = compare_work(work_fn1, work_fn2)
	print(res)
