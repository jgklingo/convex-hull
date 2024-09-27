# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point


def base_convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the convex hull of a length 2 or 3 list of points in clockwise order"""
    pass


def divide_points(points: list[tuple[float, float]]) -> list[list[tuple[float, float]]]:
    """Return the points divided vertically into two, returned as a list of length 2"""
    pass


def upper_common_tangent(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the two points that make up the upper common tangent of the points in the form [left hull, right hull]"""
    pass


def lower_common_tangent(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the two points that make up the lower common tangent of the points in the form [left hull, right hull]"""
    pass


def circle_traverse(points: list[tuple[float, float]], start: tuple[float, float], end: tuple[float, float]) -> list[tuple[float, float]]:
    """Return list of points circularly clockwise from the start to the end inclusive"""
    pass


def merge_hulls(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the merged convex hull of the two provided hulls"""
    upper_ct = upper_common_tangent(left_points, right_points)
    lower_ct = lower_common_tangent(left_points, right_points)
    return circle_traverse(left_points, lower_ct[0], upper_ct[0]) + circle_traverse(right_points, upper_ct[1], lower_ct[1])


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    if len(points) == 2 or len(points) == 3:
        return base_convex_hull(points)
    
    left_points, right_points = divide_points(points)
    left_hull = compute_hull(left_points)
    right_hull = compute_hull(right_points)
    return merge_hulls(left_hull, right_hull)
