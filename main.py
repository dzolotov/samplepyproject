def get_sum(a, b):
    return a + b


def test_sum():
    assert get_sum(3, 4) == 7


def test_failure():
    assert get_sum(3, 5) == 9
