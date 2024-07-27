"""
Given a 2D array of integers, return a list of integers representing the spiral order of the array.

TAGS:
- array
- indexing
- state transitions
- matrix
"""

TRANSITIONS = {
    # right -> down -> left -> up
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
}


def spiral(array: list[list[int]]) -> list[int]:
    row_count = len(array)
    col_count = len(array[0])

    # pos is a (row, col) iterator; this starts off the matrix
    pos = (0, -1)
    # direction indicates how to change the row_index and col_index
    # for each subsequent step
    direction = (0, 1)

    # a spiral movement has decreasing steps for each row and col,
    # and a corresponding parity switch for the direction of movement
    # e.g., a 3 row x 4 col matrix will have:
    # 4 steps R
    #                2 steps D
    # 3 steps L
    #                1 step U
    # 2 steps R
    #                0 step D
    # TERMINATE

    # use a list to keep track of the remaining steps for row movements
    # and col movements
    remaining = [row_count - 1, col_count]

    # store a counter that indicates the number of moves to take (decrease to 0)
    iter = col_count

    # store the results
    results = []

    while remaining[0] >= 0 and remaining[1] >= 0:
        for _ in range(iter, 0, -1):
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            results.append(array[pos[0]][pos[1]])

        if direction[0] == 0:
            # transition to rows
            remaining[1] -= 1
            iter = remaining[0]
            direction = TRANSITIONS[direction]
        else:
            # transition to cols
            remaining[0] -= 1
            iter = remaining[1]
            direction = TRANSITIONS[direction]

    return results


if __name__ == "__main__":
    result = spiral(
        [
            [4, 2, 3, 6],
            [1, 3, 4, 4],
            [5, 3, 4, 2],
        ]
    )
    print(result)
