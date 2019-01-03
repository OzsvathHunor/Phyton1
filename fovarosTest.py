from fovaros import is_guess_correct


def test_check_guess():
    assert is_guess_correct("Ljubljana", "Slovenia", {"Slovenia": "Ljubljana"}) == True
    return "test_check_guess() passed successfully."

print test_check_guess()