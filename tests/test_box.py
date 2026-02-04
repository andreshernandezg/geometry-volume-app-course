import pytest
from geometry.box import volume_box

def test_volume_box_valid_inputs():
    """
    Test volume computation for valid box dimensions.
    """
    width, height, depth = 2.0, 3.0, 4.0
    expected = 24.0
    assert volume_box(width, height, depth) == expected

def test_volume_box_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    width, height, depth = -2.0, 3.0, 4.0
    expected = -24.0
    assert volume_box(width, height, depth) == expected

def test_volume_box_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    width, height, depth = 1.1, 2.2, 3.3
    expected = width * height * depth
    assert volume_box(width, height, depth) == pytest.approx(expected, rel=1e-6)
