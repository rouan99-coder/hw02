#import pytest
import hw02  # Import the module here

# Part 3
# ===========
def test_3_1_print_fancy(capsys):
    hw02.print_fancy(10, 15, 6.0)
    captured = capsys.readouterr()
    assert 16*"*" in captured.out, "Tip: does your fancy printout begin with 16 asteriscs '*' (check spaces)?"
    assert "RESULTS:" in captured.out, "Tip: does your fancy printout have the string 'RESULTS:' (check spaces, colon)?"
    assert f"first number: {10}" in captured.out, "Tip: does your fancy printout print the first number line (check spaces, colon)?"
    assert f"second number: {15}" in captured.out, "Tip: does your fancy printout print the second number line (check spaces, colon)?"
    assert f"multadd result: {6.0}" in captured.out, "Tip: does your fancy printout print the multadd result line (check spaces, colon)?"
    assert 16*"=" in captured.out, "Tip: does your fancy printout end with 16 equal signs '=' (check spaces)?"
