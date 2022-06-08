from collections import defaultdict


def solution() -> int:
    with open("005.txt", "r") as f:
        data = [x.strip().split(" -> ") for x in f.readlines()]
        #print(data)
    counter = defaultdict(lambda: 0)

    def parse_point(point: str) -> map:
        return map(int, point.split(","))

    def is_horizontal(x1: int, x2: int) -> bool:
        return x1 == x2

    def is_vertical(y1: int, y2: int) -> bool:
        return y1 == y2

    def process_horizontal_line(x: int, start: int, end: int):
        while start <= end:
            counter[(x, start)] += 1
            start += 1

    def process_vertical_line(y: int, start: int, end: int):
        while start <= end:
            counter[(start, y)] += 1
            start += 1

    def process_diagonal_line(x1: int, y1: int, x2: int, y2: int):
        # Lines are at a 45-degree angle so just choose a starting point, it doesn't matter
        x_start, y_start = x1, y1

        # Now determine the direction of travel, essentially slope
        x_delta = -1 if x2 < x1 else 1
        y_delta = -1 if y2 < y1 else 1

        # We start and go on until we reach the other side
        while x_start != x2 and y_start != y2:
            counter[(x_start, y_start)] += 1
            x_start += x_delta
            y_start += y_delta

        # add the last point to counter
        #if x_start == x2 and y_start == y2:
        counter[(x_start, y_start)] += 1

    def process_lines(points: list[list[str]], diagonal: bool = False):
        for start, end in points:
            x1, y1 = parse_point(start)
            x2, y2 = parse_point(end)

            if is_horizontal(x1, x2):
                process_horizontal_line(x1, min(y1, y2), max(y1, y2))
            elif is_vertical(y1, y2):
                process_vertical_line(y1, min(x1, x2), max(x1, x2))
            elif diagonal:  # False for first part, True for second
                process_diagonal_line(x1, y1, x2, y2)

    def first_part():
        process_lines(data)

        return sum(1 for count in counter.values() if count > 1)

    def second_part():
        process_lines(data, True)

        return sum(1 for count in counter.values() if count > 1 )

    return second_part()

'''
----------------------------------------------------
'''

def two_bucket_solution():
    with open("005.txt", "r") as f:
        data = [x.strip().split(" -> ") for x in f.readlines()]

    first_bucket = set()

    second_bucket = set()

    def parse_point(point: str) -> map:
        return map(int, point.split(","))

    def is_horizontal(x1: int, x2: int) -> bool:
        return x1 == x2

    def is_vertical(y1: int, y2: int) -> bool:
        return y1 == y2

    def process_horizontal_line(x: int, start: int, end: int):
        while start <= end:
            if (x, start) not in first_bucket:
                first_bucket.add((x, start))
            elif (x, start) not in second_bucket:
                second_bucket.add((x, start))
            start += 1

    def process_vertical_line(y: int, start: int, end: int):
        while start <= end:
            if (start, y) not in first_bucket:
                first_bucket.add((start, y))
            elif (start, y) not in second_bucket:
                second_bucket.add((start, y))
            start += 1

    def process_diagonal_line(x1: int, y1: int, x2: int, y2: int):
        # Lines are at a 45-degree angle so just choose a starting point
        x_start, y_start = x1, y1
        # Now determine the direction of travel, essentially slope
        x_delta = -1 if x2 <= x1 else 1
        y_delta = -1 if y2 <= y1 else 1

        # We start and just go ahead until we reach the other side
        while x_start != x2 and y_start != y2:
            if (x_start, y_start) not in first_bucket:
                first_bucket.add((x_start, y_start))
            elif (x_start, y_start) not in second_bucket:
                second_bucket.add((x_start, y_start))
            x_start += x_delta
            y_start += y_delta

        # correction to add the last point on the other side.
        if (x_start, y_start) not in first_bucket:
            first_bucket.add((x_start, y_start))
        elif (x_start, y_start) not in second_bucket:
            second_bucket.add((x_start, y_start))


    def process_lines(points: list[list[str]], diagonal: bool = False):
        for start, end in points:
            x1, y1 = parse_point(start)
            x2, y2 = parse_point(end)

            if is_horizontal(x1, x2):
                process_horizontal_line(x1, min(y1, y2), max(y1, y2))
            elif is_vertical(y1, y2):
                process_vertical_line(y1, min(x1, x2), max(x1, x2))
            elif diagonal:  # False for first part, True for second
                process_diagonal_line(x1, y1, x2, y2)

    def first_part():
        process_lines(data)

        return len(second_bucket)

    def second_part():
        process_lines(data, True)

        return (len(first_bucket), len(second_bucket))

    return second_part()


if __name__ == "__main__":
    import timeit as t

    print("2_buckets ", two_bucket_solution())
    print(t.timeit(two_bucket_solution, number=1))
    print("solution ", solution())
    print(t.timeit(solution, number=1))
