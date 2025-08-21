"""C. Cut and Count"""


def common_letters_count(left: str, right: str) -> int:
    """Return the count of common letters between two strings."""
    common_letters = set(left).intersection(set(right))
    return len(common_letters)


tlength = int(input())
text = input()[0:tlength]

common_count = []
for cut in range(1, tlength):
    left_part = text[0:cut]
    right_part = text[cut:tlength]
    count = common_letters_count(left_part, right_part)
    common_count.append(count)

print(max(common_count))
