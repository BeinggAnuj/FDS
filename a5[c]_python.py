def longest_word(string):
    words = string.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def find_substring_index(string, substring):
    index = string.find(substring)
    return index

def count_word_occurrences(string):
    words = string.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    string = input("Enter a string: ")

    # Finding the word with the longest length
    longest = longest_word(string)
    print(f"The longest word is: {longest}")

    # Finding the index of the first appearance of a substring
    substring = input("Enter a substring to find its first appearance: ")
    index = find_substring_index(string, substring)
    if index != -1:
        print(f"The substring '{substring}' first appears at index {index}")
    else:
        print(f"The substring '{substring}' is not found in the string.")

    # Counting the occurrences of each word
    word_count = count_word_occurrences(string)
    print("Word occurrences in the string:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
