from calculador import Calculator

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(10, 2) == 5
    assert calc.divide(0, 5) == 0

    with pytest.raises(ValueError):
        calc.divide(10, 0)