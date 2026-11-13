import string


def count_word_occurrences(filename, target_word):
    word_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                words = line.split()

                for word in words:
                    cleaned_word = word.strip(string.punctuation)

                    if cleaned_word.lower() == target_word.lower():
                        word_count += 1

        return word_count

    except FileNotFoundError:
        print("File not found.")
        return 0


print(count_word_occurrences("sample.txt", "python"))
