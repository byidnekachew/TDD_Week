import pytest

@pytest.fixture
def player():
    return {"health": 70, "max_health": 100, "alive": True}

@pytest.fixture
def new_game():
    return {"score": 0, "level": 1, "active": True}