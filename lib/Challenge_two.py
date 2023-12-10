def exactly_two_positive(a, b, c):
    # Count the number of positive integers
    positive_count = 0

    # Check each number and increment the positive_count if it's positive
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two of the three integers are positive, and False otherwise
    return positive_count == 2


# test cases 
print (exactly_two_positive(1, 1, -1)) # True