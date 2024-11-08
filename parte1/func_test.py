import pytest

from func import es_primo

# Returns True for a list of prime numbers including 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
def test_returns_true_for_prime_numbers_extended():
  assert es_primo(2) == True
  assert es_primo(3) == True
  assert es_primo(5) == True
  assert es_primo(7) == True
  assert es_primo(11) == True
  assert es_primo(13) == True
  assert es_primo(17) == True
  assert es_primo(19) == True
  assert es_primo(23) == True
  assert es_primo(29) == True
  assert es_primo(31) == True

# Returns False for non-prime numbers like 0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20
def test_returns_false_for_non_prime_numbers_extended():
    assert es_primo(0) == False
    assert es_primo(1) == False
    assert es_primo(4) == False
    assert es_primo(6) == False
    assert es_primo(8) == False
    assert es_primo(9) == False
    assert es_primo(10) == False
    assert es_primo(12) == False
    assert es_primo(14) == False
    assert es_primo(15) == False
    assert es_primo(16) == False
    assert es_primo(18) == False
    assert es_primo(20) == False

# Raises TypeError for non-numeric inputs
def test_type_error_for_non_integer_values():
    # Ensure the environment is correctly set up and no file system issues exist
    try:
        with pytest.raises(TypeError):
            es_primo(2.3)
        with pytest.raises(TypeError):
            es_primo(3.9)
        with pytest.raises(TypeError):
            es_primo("three")
        with pytest.raises(TypeError):
            es_primo(None)
        with pytest.raises(TypeError):
            es_primo(True)
        with pytest.raises(TypeError):
            es_primo(False)
    except OSError as e:
        pytest.fail(f"Environment setup issue: {e}")

# The function must determine that all negative numbers are not prime. This includes the numbers -1, -2, -3, -5, -11, -13.
def test_negative_numbers_are_not_prime():
    assert es_primo(-1) == False
    assert es_primo(-2) == False
    assert es_primo(-3) == False
    assert es_primo(-5) == False
    assert es_primo(-11) == False
    assert es_primo(-13) == False

# The function must be able to efficiently evaluate the primality of large numbers, and determine that 1000003 is prime and that 1000004 is not prime.
def test_large_number_primality():
    assert es_primo(1000003) == True
    assert es_primo(1000004) == False

# The function must throw a type error (TypeError) when confronted with unusual entries such as the string “five”, None, and empty lists ([]).
def test_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        es_primo("five")
    with pytest.raises(TypeError):
        es_primo(None)
    with pytest.raises(TypeError):
        es_primo([])

# The function must be able to handle and pass as primes floating point numbers that are extremely close to integer primes, such as 19.000000000000004 and 23.000000000000004, recognizing their primality.
def test_floating_point_near_primes():
    assert es_primo(int(19.000000000000004)) == True
    assert es_primo(int(23.000000000000004)) == True