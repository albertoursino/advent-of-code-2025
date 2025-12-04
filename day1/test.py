from utils import pass_from_zero


def test_pass_from_zero():
    assert pass_from_zero(50, "R", 60) == 1
    assert pass_from_zero(50, "R", 60) == 1
    assert pass_from_zero(50, "R", 150) == 2
    assert pass_from_zero(0, "R", 100) == 1
    assert pass_from_zero(0, "R", 250) == 2
    assert pass_from_zero(50, "L", 60) == 1
    assert pass_from_zero(50, "L", 150) == 2
    assert pass_from_zero(50, "L", 50) == 1
    assert pass_from_zero(50, "R", 50) == 1
    assert pass_from_zero(0, "L", 100) == 1
    assert pass_from_zero(0, "L", 250) == 2
    assert pass_from_zero(0, "L", 230) == 2
    assert pass_from_zero(0, "R", 20) == 0
    assert pass_from_zero(0, "L", 20) == 0
    assert pass_from_zero(1, "L", 2) == 1
    assert pass_from_zero(1, "R", 100) == 1
    assert pass_from_zero(1, "L", 100) == 1


if __name__ == "__main__":
    test_pass_from_zero()
    print("All tests passed.")
