def fizzbuzz(n):
    """
    # Original test 1 code, solves test 1 but not 2
    if n == 3:
        return "Fizz"


    # Original test 3 code, solves test 3 but not 4
    if n == 5:
        return "Buzz"

    # Original test 5 code, solves test 5 but not 6
    if n == 15:
        return "FizzBuzz"
    """

    if n % 15 == 0:
        return "FizzBuzz"

    # Solves Test 1 and 2:
    if n % 3 == 0:
        return "Fizz"

    # Solves Test 3 and 4:
    if n % 5 == 0:
        return "Buzz"


def test_fizz():
    # First Test.
    assert fizzbuzz(3) == "Fizz"


def test_fizz_again():
    # Second Test.
    assert fizzbuzz(6) == "Fizz"


def test_buzz():
    # Third Test.
    assert fizzbuzz(5) == "Buzz"


def test_buzz_again():
    # Fourth test.
    assert fizzbuzz(10) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_again():
    assert fizzbuzz(30) == "FizzBuzz"