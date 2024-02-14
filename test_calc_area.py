from pytest import approx
from pytest import raises

def test_calc_area_square():
    from calc_area_circle import calc_area_square

    input_numbers = [0, 1, 4, 100]
    output_numbers = [0, 1, 16, 10000]
    assert len(input_numbers) == len(output_numbers)

    # option 1
    for input, output in zip(input_numbers, output_numbers):
        assert calc_area_square(input) == output

    # option 2
    for i in range(len(input_numbers)):
        this_input = input_numbers[i]
        this_exp_out = output_numbers[i]

        assert calc_area_square(this_input) == this_exp_out

def test_calc_area_circle():
    from calc_area_circle import calc_area_circle

    assert calc_area_circle(2) == approx(12.5663, abs=1e-3)

from calc_area_circle import calc_area_circle
def test_calc_area_circle_errors():
    with raises(ValueError):
        calc_area_circle(-1)
    with raises(TypeError):
        calc_area_circle('this is not a number')