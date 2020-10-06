# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # urls = {}
    result = []

    for x in files:
        # if x not in urls:
        #     urls[x] = True
        for c in queries:
            if x.find(c) >= 0:
                result.append(x)

    
    # print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
