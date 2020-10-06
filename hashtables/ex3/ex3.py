def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dups = []
    numbers = {}
    seen = {}
    result= []

    for x in arrays:
        for c in x:
            if c not in numbers:
            
                numbers[c] = True
            else:
                dups.append(c)
                for a in dups:
                    if a not in seen:
                        result.append(a)
                        seen[a] = True
    # print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
