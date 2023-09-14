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
