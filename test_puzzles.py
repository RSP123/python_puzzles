import pytest
from three_variable import largest
from prime_num import prime_number
from gcd import gcd


@pytest.mark.parametrize("input_1, input_2, input_3, expected_output",
                            [
                                (3, 5, 9, 9),
                                (2, 1, 3, 3),
                                (8, 2, 2, 8),
                                (5, 1, 3, 5),
                                (2, 8, 3, 8),
                                (9, 3, 9, 9),
                                (2, 2, 2, 2)
                            ]
                        )
def test_largest(input_1, input_2, input_3, expected_output):
    assert largest(input_1, input_2, input_3) == expected_output



@pytest.mark.parametrize("input, expected_output",
                            [
                                (2, True),
                                (3, True),
                                (5, True),
                                (9, False),
                                (10, False),
                                (11, True),
                                (19, True),
                                (1, True)
                            ]
                        )
def test_prime_number(input, expected_output):
    assert prime_number(input) == expected_output


@pytest.mark.parametrize("input_1, input_2,expected_output",
                            [
                               (48, 68, 4),
                               (12, 45, 3),
                               (10, 20, 10),
                               (24, 52, 4),
                               (62, 24, 2)
                            ]

                        )


def test_gcd(input_1,input_2,expected_output):
    assert gcd(input_1, input_2) == expected_output
