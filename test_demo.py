import pytest

@pytest.fixture
def sample():
    print("\nBefore Test")
    yield
    print("\nAfter Test")

def test_sample(sample):
    print("Executing Test")