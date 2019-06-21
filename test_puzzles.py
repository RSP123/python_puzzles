import pytest
from three_variable import largest
from prime_num import prime_number
from gcd import gcd
from circle_circumference import circumference_circle, area_circle
from lcm import lcm
from email_check import email_check
from largest_list import largest_list
from factorial_series import factorial
from fibonacci_series import fibonacci
from greeting_msg import greeting
from palindrome import palindrom
from radius_circle import radius_of_circle
from string_length import string_function
from first_last_in_new_list import new_list
from odd_even_list import odd_even
from backward_string import backward
from next_prime import is_prime
from denomination import denomination
from minus_duplicates import duplicate
from birthday_dictionary import birthday
from sort_and_find import sort_find


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


@pytest.mark.parametrize("input_1,expected_output",
                             [
                               (4, 25.1200),
                               (7, 43.960),
                               (14, 87.920),
                               (16, 100.48),
                               (34, 213.520)
                             ]
                        )
def test_circumference_circle(input_1, expected_output):
    assert circumference_circle(input_1) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                             [
                                (4, 50.240),
                                (7, 153.860),
                                (14, 615.440),
                                (16, 803.840),
                                (34, 3629.840)

                             ]
                        )
def test_area_circle(input_1,expected_output):
    assert area_circle(input_1) == expected_output

@pytest.mark.parametrize("input_1,input_2,expected_output",
                            [
                               (6, 4, 12),
                               (63, 43, 2709),
                               (23, 46, 46),
                               (56, 35, 280),
                               (78, 23, 1794)
                            ]
                        )
def test_lcm(input_1,input_2,expected_output):
    assert lcm(input_1,input_2) == expected_output

# @pytest.mark.parametrize("input_1,expected_output",
#                               [
#                                ("pradeep.rs@hotmail.com",True),
#                                (jayanth@s@hotmail.com, False),
#                                (krishoth.m@hotmail.com, True),
#                                (hem-a@hotmail.com, False),
#                                (pradeep323@gmail.com, True)
#                               ]
#                         )
# def test_email_check(input_1,expected_output):
#     assert email_check(input_1) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                              [
                                 ([23, 3, 14], 23),
                                 ([34, 56, 2], 56),
                                 ([203, 45, 67], 203),
                                 ([12, 45, 78], 78),
                                 ([3, 45, 56], 56),
                                 ([45, 45, 8], 45),
                                 ([34, 35, 56], 56)
                              ]
                        )

def test_largest_list(input_1,expected_output):
    assert largest_list(input_1) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                             [
                                (5, 120),
                                (1, 1),
                                (3, 6),
                                (12, 479001600),
                                (9, 362880),
                                (7, 5040)
                             ]
                        )
def test_factorial(input_1,expected_output):
    assert factorial(input_1) == expected_output


@pytest.mark.parametrize("input_1,expected_output",
                             [
                                (5, 5),
                                (12, 144),
                                (23, 28657),
                                (8, 21),
                                (15, 610),
                                (18, 2584)
                             ]
                        )
def test_fibonacci(input_1,expected_output):
    assert fibonacci(input_1) == expected_output



@pytest.mark.parametrize("input_1,expected_output",
                              [
                                ("pradeep rs", "Hi pradeep!"),
                                ("jayanth sn", "Hi jayanth!"),
                                ("krishoth m", "Hi krishoth!"),
                                ("hema rs", "Hi hema!"),
                                ("divya rs", "Hi divya!"),
                                ("monika rs", "Hi monika!"),
                                ("pooja rs", "Hi pooja!")

                              ]
                        )
def test_greeting(input_1,expected_output):
    assert greeting(input_1) == expected_output


@pytest.mark.parametrize("input_1,expected_output",
                            [
                              ("asdsa", True),
                              ("asfsfg", False),
                              ("hellleh", True),
                              ("malayalam", True),
                              ("tamil", False)
                            ]
                        )
def test_palindrom(input_1,expected_output):
    assert palindrom(input_1) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                             [
                               (4, 1.129),
                               (5, 1.262),
                               (12, 1.955),
                               (8, 1.596),
                               (45, 3.786),
                               (56, 4.223)
                             ]
                        )
def test_radius_of_circle(input_1,expected_output):
    assert radius_of_circle(input_1) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                            [
                              ("pradeep", 7),
                              ("jayanth sn", 10),
                              ("i love chennai", 14),
                              ("iam indian", 10)
                            ]
                        )
def test_string_function(input_1,expected_output):
    assert string_function(input_1) == expected_output


@pytest.mark.parametrize("input_1,expected_output",
                                [
                                  ([12, 34, 45, 46, 56], [12, 56]),
                                  ([34, 35, 67, 45, 89], [34, 89]),
                                  ([56, 2, 4, 6, 342], [56, 342]),
                                  ([359, 23, 45, 34, 253], [359, 253]),
                                  ([349, 23, 456, 34, 56], [349, 56]),
                                  ([9, 3, 5, 4, 23], [9, 23]),
                                  ([4, 23, 45, 34, 6], [4, 6])


                                ]
                        )

def test_new_list(input_1,expected_output):
    assert new_list(input_1) == expected_output

@pytest.mark.parametrize("input,expected_output",
                            [
                             ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]),
                             ( [1, 24, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 24, 4, 6, 8, 10]),
                             ( [1, 22, 3, 5, 5, 63, 76, 88, 69, 10], [1, 3, 5, 5, 63, 69, 22, 76, 88, 10]),
                             ( [1, 26, 3, 34, 5, 56, 7, 28, 2, 10], [1, 3, 5, 7, 26, 34, 56, 28, 2, 10])
                            ]
                        )
def test_odd_even(input,expected_output):
    assert odd_even(input) == expected_output

@pytest.mark.parametrize("input_1,expected_output",
                             [
                               ("chennai from pradeep im hello hii", "hii hello im pradeep from chennai"),
                               ("chennai", "chennai"),
                               ("i love india", "india love i"),
                               ("software engineer", "engineer software" )
                             ]
                        )
def test_backward(input_1,expected_output):
    assert backward(input_1) == expected_output

@pytest.mark.parametrize("input,expected_output",
                            [
                               (2, 3),
                               (3, 5),
                               (11, 13),
                               (17, 19),
                               (6, 7)
                            ]
                        )
def test_is_prime(input,expected_output):
    assert is_prime(input) == expected_output

@pytest.mark.parametrize("input,expected_output",
                            [
                               (10900, [(2000, 5), (500, 1), (200, 2)]),
                               (2900, [(2000, 1), (500, 1), (200, 2)]),
                               (4235, [(2000, 2), (200, 1), (20, 1),(10, 1),(5, 1)])
                            ]
                        )
def test_denomination(input,expected_output):
    assert denomination(input) == expected_output


@pytest.mark.parametrize("input,expected_output",
                             [
                               ([1, 2, 2, 3, 5, 5, 4, 6], [1, 2, 3, 4, 5, 6]),
                               ([1, 1, 2, 3, 3, 4, 4, 3], [1, 2, 3, 4]),
                               ([1, 1, 12, 23, 34, 34, 45] , [1, 34, 12, 45, 23]),
                               ([45, 45, 67, 78, 78, 78, 78], [67, 45, 78,])
                             ]
                        )
def test_duplicate(input, expected_output):
    assert duplicate(input) == expected_output


@pytest.mark.parametrize("input,expected_output",
                           [
                              ("pradeep", "28-5-1994"),
                              ("krishoth", "16-3-1996"),
                              ("jayanth", "20-1-1996"),
                              ("hema", "31-6-1995")
                           ]
                       )
def test_birthday(input,expected_output):
    assert birthday(input) == expected_output


@pytest.mark.parametrize("input,input_1,expected_output",
                            [
                                ([1, 2, 3, 4, 5, 6, 7, 8],3, True)
                            ]
                        )
def test_sort_find(input,input_1,expected_output):
    sort_find(input,input_1) == expected_output
