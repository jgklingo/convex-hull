from convex_hull import circle_traverse

def circle_traverse_test():
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    start = (0, 0)
    end = (0, 1)
    assert circle_traverse(points, start, end) == [(0, 0), (1, 0), (1, 1), (0, 1)]
    start = (1, 0)
    end = (1, 1)
    assert circle_traverse(points, start, end) == [(1, 0), (1, 1)]
    start = (1, 1)
    end = (0, 0)
    assert circle_traverse(points, start, end) == [(1, 1), (0, 1), (0, 0)]
    start = (0, 1)
    end = (1, 0)
    assert circle_traverse(points, start, end) == [(0, 1), (0, 0), (1, 0)]

circle_traverse_test()