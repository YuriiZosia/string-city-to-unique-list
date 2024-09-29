import pytest

from point_class import Point


def test_point_class_attribute_exist():
    assert hasattr(
        Point, "points"
    ), "Class Point should have class attribute points"


@pytest.mark.parametrize(
    "points,points_len",
    [
        ((), 0),
        (((1, 2),), 1),
        (((1, 2), (3, 4), (-3, -4), (9, -2)), 4),
    ],
)
def test_point_class_attribute_addition(points, points_len):
    Point.points = []
    for point in points:
        Point(*point)
    assert all(
        [isinstance(point, Point) for point in Point.points]
    ), "Point.points should consist of Point instances"
    assert len(Point.points) == points_len, (
        f"'len(Point.points)' should equal to {points_len}, "
        f"when tuple of points coordinates of created Point instances equals to {points}"
    )


@pytest.mark.parametrize(
    "point,result",
    [
        ((0, 0), 0),
        ((1, 2), 2.24),
        ((3, 4), 5),
        ((-4, -8), 8.94),
    ],
)
def test_point_distance_to_origin(point, result):
    point_inst = Point(*point)
    assert point_inst.distance_to_origin() == result, (
        f"Distance to origin should equal to {result}, "
        f"when point coordinates is {point}"
    )


@pytest.mark.parametrize(
    "point,point2,result",
    [
        ((1, 2), (0, 0), 2.24),
        ((3, 4), (-5, -1), 9.43),
        ((-4, -8), (10, 0), 16.12),
        ((-1, -2), (-4, -6), 5.0)
    ],
)
def test_point_distance_to_point(point, point2, result):
    point_1 = Point(*point)
    point_2 = Point(*point2)
    assert point_1.distance_to_point(point_2) == result, (
        f"'point_1.distance_to_point(point_2)' should equal to {result}, "
        f"when point_1 coordinates is {point},"
        f"and point_2 coordinates is {point2}"
    )


@pytest.mark.parametrize(
    "point,result",
    [((0, 0), 0), ((1, 2), 2), ((3, -4), 4), ((-4, 8), 8), ((-10, -12), 12)],
)
def test_point_distance_to_x_axis(point, result):
    point_inst = Point(*point)
    assert point_inst.distance_to_x_axis() == result, (
        f"Distance to X axis should equal to {result}, "
        f"when point coordinates is {point}"
    )


@pytest.mark.parametrize(
    "point,result",
    [((0, 0), 0), ((1, 2), 1), ((3, -4), 3), ((-4, 8), 4), ((-10, -12), 10)],
)
def test_point_distance_to_y_axis(point, result):
    point_inst = Point(*point)
    assert point_inst.distance_to_y_axis() == result, (
        f"Distance to Y axis should equal to {result}, "
        f"when point coordinates is {point}"
    )


def test_point_find_closest_point_returns_none_for_only_one_point():
    Point.points = []
    point = Point(1, 3)
    assert point.find_closest_point() is None, (
        "If there are only one point, 'find_closest_point' should return 'None' "
        "for this point"
    )


@pytest.mark.parametrize(
    "point,another_points,correct_point",
    [
        ((1, 3), [(-10, -10)], (-10, -10)),
        ((1, 2), [(2, 3), (-2, -3), (4, 4)], (2, 3)),
        ((3, 10), [(-4, -8), (-2, 24), (-3, 3)], (-3, 3)),
    ],
)
def test_point_find_closest_point_returns_correct_point(
    point, another_points, correct_point
):
    Point.points = []
    for point_ in another_points:
        Point(*point_)
    point = Point(*point)
    closest_point = point.find_closest_point()
    assert (closest_point.x, closest_point.y) == correct_point, (
        f"'point.find_closest_point' should return {correct_point}, "
        f"when point coordinates is {point}, and "
        f"another points coordinates: {another_points}"
    )
