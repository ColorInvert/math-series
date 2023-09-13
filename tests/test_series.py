import pytest

from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


def test_fib_exists():
  assert fibonacci


#test various input values for fibonacci
def test_fib_0():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected


def test_fib_3():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected


def test_fib_5():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected


def test_fib_7():
  actual = fibonacci(7)
  expected = 13
  assert actual == expected


def test_lucas_exists():
  assert lucas

#test various input values for lucas series
def test_lucas_0():
  actual = lucas(0)
  expected = 2
  assert actual == expected

  
def test_lucas_1():
  actual = lucas(1)
  expected = 1
  assert actual == expected


def test_lucas_3():
  actual = lucas(3)
  expected = 4
  assert actual == expected


def test_lucas_5():
  actual = lucas(5)
  expected = 11
  assert actual == expected


def test_lucas_7():
  actual = lucas(7)
  expected = 29
  assert actual == expected


def test_sum_series_exists():
  assert sum_series


#test various input values for sum series, assuming no optional arguments provided
def test_sum_series_no_optionals_0():
  actual = sum_series(0)
  expected = 0
  assert actual == expected


def test_sum_series_no_optionals_1():
  actual = sum_series(1)
  expected = 1
  assert actual == expected


def test_sum_series_no_optionals_2():
  actual = sum_series(2)
  expected = 1
  assert actual == expected


def test_sum_series_no_optionals_7():
  actual = sum_series(7)
  expected = 13
  assert actual == expected


#test various input values for sum series, with optional inputs entered matching the Lucas series.
def test_sum_series_sim_lucas_0():
  actual = sum_series(0,2,1)
  expected = 2
  assert actual == expected


def test_sum_series_sim_lucas_1():
  actual = sum_series(1,2,1)
  expected = 1
  assert actual == expected


def test_sum_series_sim_lucas_2():
  actual = sum_series(2,2,1)
  expected = 3
  assert actual == expected


def test_sum_series_sim_lucas_7():
  actual = sum_series(7,2,1)
  expected = 29
  assert actual == expected