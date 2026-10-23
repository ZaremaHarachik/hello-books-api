
import pytest

# Fixture to provide an empty list for testing
@pytest.fixture
def empty_list():
    return []

# Test function to check the length of the empty list fixture
def test_len_of_empty_list(empty_list):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0


# Fixture to provide a list with one item for testing
@pytest.fixture
def one_item(empty_list):
    empty_list.append("item")
    return empty_list

# Test function to check the length of the one_item fixture
def test_len_of_unary_list(one_item):
    assert isinstance(one_item, list)
    assert len(one_item) == 1
    assert one_item[0] == "item"


# Fixture to provide a list with multiple items for testing
class FancyObject:
    def __init__(self):
        self.fancy = True
        print(f"\nFancyObject: {self.fancy}")

    def or_is_it(self):
        self.fancy = not self.fancy

    def cleanup(self):
        print(f"\ncleanup: {self.fancy}")


# Fixture to provide a fancy object for testing
@pytest.fixture
def so_fancy():
    fancy_object = FancyObject()

    yield fancy_object

    fancy_object.cleanup()
    

# Test function to check the behavior of the so_fancy fixture
def test_so_fancy(so_fancy):
    assert so_fancy.fancy
    so_fancy.or_is_it()
    assert not so_fancy.fancy

