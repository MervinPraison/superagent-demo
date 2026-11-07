from invoice import total


def test_total_adds_ten_percent_tax():
    assert total([(10.0, 2), (5.0, 1)]) == 27.5
