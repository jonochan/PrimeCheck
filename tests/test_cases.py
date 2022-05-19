import pytest
import PrimeFinder


def test_negative():
    assert PrimeFinder.is_prime(-1) == "Please enter a number greater than 2"

def test_even():
    assert PrimeFinder.is_prime(8) == "Number is not prime"

def test_three():
    assert PrimeFinder.is_prime(3) == "Number is prime"

def test_large_even():
    assert PrimeFinder.is_prime(12948641192868) == "Number is not prime"

def test_large_prime():
    assert PrimeFinder.is_prime(7919) == "Number is prime"
