from calculador import Calculator

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 0) == 0