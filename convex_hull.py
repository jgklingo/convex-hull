# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point


def base_convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the convex hull of a length 2 or 3 list of points in clockwise order"""
    pass


def divide_points(points: list[tuple[float, float]]) -> list[list[tuple[float, float]]]:
    """Return the points divided vertically into two, returned as a list of length 2"""
    pass


def upper_ct(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the two points that make up the upper common tangent of the points in the form [left hull, right hull]"""
    pass


def lower_ct(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the two points that make up the lower common tangent of the points in the form [left hull, right hull]"""
    pass


def circle_traverse(points: list[tuple[float, float]], start: tuple[float, float], target: tuple[float, float]) -> list[tuple[float, float]]:
    """List the points circularly clockwise from the start to the target inclusive"""
    pass


def merge_hulls(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the merged convex hull of the two provided hulls"""
    pass


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    return []
