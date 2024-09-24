frankenstein = open("books/frankenstein.txt", "r")
frankenstein = frankenstein.read()
import collections
import string
def total_words(book):
    return len(book.split())

def character_count(book):
    alpha_dict = {letter: 0 for letter in string.ascii_lowercase}
    book = book.lower()
    for letter in book:
        if letter in alpha_dict:
            alpha_dict[letter] += 1
    return alpha_dict


def print_report(book):
    count = total_words(book)
    letters = character_count(book)
    print("    --- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for items in letters.keys():
        print(f"The {items} character was found {letters[items]} times")

    print("--- End report ---")

print_report(frankenstein)
        