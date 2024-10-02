def pascal_triangle(n):
    triangle = [[1]]
    i = 1
    if n <= 1:
        return []
    while i < n:
        array = []
        for index in range(i + 1):
            prev = triangle[i - 1][index - 1] if index > 0 else 0
            current = triangle[i - 1][index] if index != len(triangle[i - 1]) else 0
            array.append(prev + current)
        i += 1
        triangle.append(array)
    return triangle
