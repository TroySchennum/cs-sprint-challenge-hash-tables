def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = {}
    result = []
    for x in a:
        x = abs(x)
        if x not in numbers:
            
            numbers[x] = True
        else:
            result.append(x)
    # print(result)
    # print(numbers)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
