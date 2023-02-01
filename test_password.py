def is_strong_password(string):
    # Set initial Variables
    passes = True
    num_count = 0
    cap_count = 0
    spc_count = 0

    # Run loop to check for certain characters
    for char in string:
        if char.isnumeric():
            num_count += 1
        if char.isupper():
            cap_count += 1
        if not char.isalnum():
            spc_count += 1

    # Print required fields and set test to fail.
    if len(string) < 8:
        print("\nPassword must be at least 8 characters")
        passes = False

    if num_count < 2:
        print("\nPassword must contain at least 2 numbers")
        passes = False

    if cap_count < 1:
        print("\nPassword must contain at least one capital letter")
        passes = False

    if spc_count < 1:
        print("\nPassword must contain at least one special character")
        passes = False

    # If no issues are found, return successfully.
    return passes

# Test 1, checks for required password length.
def test_length():
    assert is_strong_password("pass") == False

# Test 2, checks if a password contains numbers.
def test_numbers():
    assert is_strong_password("longenough") == False

# Test 3, checks if there is a capital letter in the password.
def test_capital():
    assert is_strong_password("whales12") == False

# Test 4, Checks for special characters.
def test_special():
    assert is_strong_password("Largecows532") == False

# Test 5, Checks if a password passing all requirements is accepted.
def test_correct():
    assert is_strong_password("RichGuy$99") == True