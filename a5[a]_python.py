def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def character_frequency(sentence, char):
    count = 0
    for ch in sentence:
        if ch == char:
            count += 1
    return count


def is_palindrome(sentence):
    sentence = sentence.replace(" ", "").lower()
    return sentence == sentence[::-1]


def main():
    sentence = input("Enter a string: ")

    longest = longest_word(sentence)
    print(f"The longest word is: {longest}")

    char = input("Enter a character to find its frequency: ")
    frequency = character_frequency(sentence, char)
    print(f"The frequency of '{char}' is: {frequency}")

    if is_palindrome(sentence):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
