def count_word_occurrences(filename, target_word):
    word_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.strip().split(" ")

                for word in words:
                    if word.lower() == target_word.lower():
                        word_count += 1

        return word_count

    except FileNotFoundError:
        print("File not found.")
        return 0


print(count_word_occurrences("sample.txt", "python"))