#import pytest
import hw02  # Import the module here

# Part 1
# ===========
def test_1_1_read_two_ints(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["10", "15"])
    exp1a, exp1b = 10, 15
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret1a, ret1b = hw02.read_two_ints()
        captured = capsys.readouterr()

        assert ret1a == exp1a, "Tip: Did you cast the x value to int?"
        assert ret1b == exp1b, "Tip: Did you cast the y value to int?"