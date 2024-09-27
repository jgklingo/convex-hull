from convex_hull import circle_traverse

def circle_traverse_test():
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    start = 0
    end = 3
    assert circle_traverse(points, start, end) == [(0, 0), (1, 0), (1, 1), (0, 1)]
    start = 1
    end = 2
    assert circle_traverse(points, start, end) == [(1, 0), (1, 1)]
    start = 2
    end = 0
    assert circle_traverse(points, start, end) == [(1, 1), (0, 1), (0, 0)]
    start = 3
    end = 1
    assert circle_traverse(points, start, end) == [(0, 1), (0, 0), (1, 0)]

circle_traverse_test()