def first_substring_index(string, substring):
    return string.find(substring)

def count_word_occurrences(string):
    words = string.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def copy_string(string):
    return string[:]

def main():
    string = input("Enter a string: ")

    substring = input("Enter the substring to find: ")
    index = first_substring_index(string, substring)
    if index != -1:
        print(f"The substring first appears at index: {index}")
    else:
        print("The substring was not found.")

    word_count = count_word_occurrences(string)
    print("Word occurrences in the string:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

    copied_string = copy_string(string)
    print(f"Copied string: {copied_string}")

if __name__ == "__main__":
    main()
