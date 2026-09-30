#import pytest
import hw02  # Import the module here

# Part 2
# ===========
def test_2_2_compute_multadd(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["8", "2"])
    exp2 = 1.6
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret2 = hw02.compute_multadd(8, 2)
        captured = capsys.readouterr()

        assert ret2 == exp2, "Tip: Is the expression correct (value and type)?"
        assert "mult result: 16" in captured.out, "Tip: is your mult printout correctly formatted (case, spaces)?"
        assert "add result: 10" in captured.out, "Tip: is your add printout correctly formatted (case, spaces)?"