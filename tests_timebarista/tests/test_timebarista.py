from timebarista import barista
import pytest as test


@test.mark.parametrize("orders, time", [([2, 10, 5, 3, 9], 85),
                                        ([4, 3, 2], 22),
                                        ([20, 5], 32),
                                        ([], 0),
                                        ([20, 5, 4, 3, 1, 5, 7, 8], 211),
                                        ([5, 4, 3, 2, 1], 55)])
def test_case(orders, time):
    assert barista(orders) == time
