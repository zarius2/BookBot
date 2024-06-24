def main():
    actual_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    total_words = len(words)
    letter_counts = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    print("----------BOOK REPORT----------")
    print(f"{total_words} word(s) were found in the document.")
    for i in actual_letters:
        print(f"The {i} character was found {letter_counts[i]} times")

main()