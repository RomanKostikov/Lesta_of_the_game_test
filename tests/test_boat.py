import pytest
from boat import Boat


@pytest.fixture
def boat():
    return Boat()


def test_row_forward(boat):
    boat.lift_anchor()
    assert boat.row_forward(5) == "Boat moved forward 5 strokes."
    assert boat.position == 5


def test_row_backward(boat):
    boat.lift_anchor()
    boat.row_forward(5)
    assert boat.row_backward(3) == "Boat moved backward 3 strokes."
    assert boat.position == 2


def test_drop_anchor(boat):
    assert boat.drop_anchor() == "Anchor dropped."
    assert boat.is_anchored


def test_lift_anchor(boat):
    boat.drop_anchor()
    assert boat.lift_anchor() == "Anchor lifted."
    assert not boat.is_anchored


def test_cannot_move_with_anchor(boat):
    boat.drop_anchor()
    assert boat.row_forward(3) == "Cannot move, anchor is down."
