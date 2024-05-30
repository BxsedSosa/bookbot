def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_count = [
        {key: value}
        for key, value in sorted(
            char_counter(text).items(), reverse=True, key=lambda item: item[1]
        )
    ]
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_counter(text)} words found in the document")
    for i in range(len(char_count)):
        keys = char_count[i].keys()
        for key in keys:
            print(f"The {key} character was found {char_count[i][key]} times")
    print("--- End report ---")


def char_counter(text):
    text = text.lower()
    char_dictonary = {}

    for char in text:
        if char.isalpha():
            if char not in char_dictonary:
                char_dictonary[char] = 1
            else:
                char_dictonary[char] += 1

    return char_dictonary


def word_counter(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
