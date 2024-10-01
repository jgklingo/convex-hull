# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point


def base_convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the convex hull of a length 2 or 3 list of points in clockwise order"""
    # AI, check this
    if len(points) == 2:
        return points
    if points[0][0] == points[1][0] == points[2][0]:
        return points
    if points[0][1] == points[1][1] == points[2][1]:
        return points
    if points[0][0] == points[1][0]:
        return [points[0], points[1], points[2]]
    if points[0][0] == points[2][0]:
        return [points[0], points[2], points[1]]
    if points[1][0] == points[2][0]:
        return [points[1], points[2], points[0]]
    if points[0][1] == points[1][1]:
        return [points[0], points[1], points[2]]
    if points[0][1] == points[2][1]:
        return [points[0], points[2], points[1]]
    if points[1][1] == points[2][1]:
        return [points[1], points[2], points[0]]
    if points[0][0] < points[1][0] < points[2][0] or points[0][0] > points[1][0] > points[2][0]:
        return [points[0], points[2], points[1]]
    return points


def divide_points(points: list[tuple[float, float]]) -> list[list[tuple[float, float]]]:
    """Return the points divided vertically into two, returned as a list of length 2"""
    return [points[:len(points) // 2], points[len(points) // 2:]]


def find_slope(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Return the slope of the line between the two points"""
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def upper_common_tangent(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]], rightmost_left: tuple[float, float], leftmost_right: tuple[float, float]) -> tuple[int, int]:
    """Return the indices of the two points that make up the upper common tangent of the points in the form [left hull, right hull]"""
    # Make sure that these functions don't cause merge_hulls to exceed O(n) time complexity
    i = left_points.index(rightmost_left)  # potential O(n) operations that could be optimized
    j = right_points.index(leftmost_right)
    shifted_right = True
    shifted_left = True
    while shifted_right or shifted_left:
        shifted_right = False
        while find_slope(left_points[(i - 1) % len(left_points)], right_points[j]) < find_slope(left_points[i], right_points[j]):
            i = (i - 1) % len(left_points)
            shifted_right = True
        shifted_left = False
        while find_slope(left_points[i], right_points[(j + 1) % len(right_points)]) > find_slope(left_points[i], right_points[j]):
            j = (j + 1) % len(right_points)
            shifted_left = True
    return i, j


def lower_common_tangent(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]], rightmost_left: tuple[float, float], leftmost_right: tuple[float, float]) -> tuple[int, int]:
    """Return the indices of the two points that make up the lower common tangent of the points in the form [left hull, right hull]"""
    i = left_points.index(rightmost_left)
    j = right_points.index(leftmost_right)
    shifted_right = True
    shifted_left = True
    while shifted_right or shifted_left:
        shifted_right = False
        while find_slope(left_points[(i - 1) % len(left_points)], right_points[j]) > find_slope(left_points[i], right_points[j]):
            i = (i - 1) % len(left_points)
            shifted_right = True
        shifted_left = False
        while find_slope(left_points[i], right_points[(j + 1) % len(right_points)]) < find_slope(left_points[i], right_points[j]):
            j = (j + 1) % len(right_points)
            shifted_left = True
    return i, j


def circle_traverse(points: list[tuple[float, float]], start: int, end: int) -> list[tuple[float, float]]:
    """Return list of points circularly clockwise from the start to the end index inclusive"""
    result = []
    i = start
    while i != end:
        result.append(points[i])
        i = (i + 1) % len(points)
    result.append(points[end])
    return result


def merge_hulls(left_points: list[tuple[float, float]], right_points: list[tuple[float, float]], rightmost_left: tuple[float, float], leftmost_right: tuple[float, float]) -> list[tuple[float, float]]:
    """Return the merged convex hull of the two provided hulls"""
    upper_ct = upper_common_tangent(left_points, right_points, rightmost_left, leftmost_right)
    lower_ct = lower_common_tangent(left_points, right_points, rightmost_left, leftmost_right)
    return circle_traverse(left_points, lower_ct[0], upper_ct[0]) + circle_traverse(right_points, upper_ct[1], lower_ct[1])


def compute_hull_helper(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    if len(points) == 2 or len(points) == 3:
        return base_convex_hull(points)
    
    left_points, right_points = divide_points(points)
    rightmost_left, leftmost_right = left_points[-1], right_points[0]
    left_hull = compute_hull_helper(left_points)
    right_hull = compute_hull_helper(right_points)
    return merge_hulls(left_hull, right_hull, rightmost_left, leftmost_right)


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    points.sort()
    return compute_hull_helper(points)
