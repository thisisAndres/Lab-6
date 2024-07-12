from calculador import Calculator

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 10) == 0