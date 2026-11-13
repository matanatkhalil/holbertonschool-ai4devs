def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


numbers = [1, 2, 2, 3, 3, 3, 4, 4]
print(remove_duplicates(numbers))
