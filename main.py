def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):

    text = text.lower()
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

def print_report(words, char_count):

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    sorted_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_count:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")    

    print(f"--- End Report ---")

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print_report(word_count,char_count)

    # for char, count in char_count:
    #     print(f"'{char}': {count}")
    
    # print(file_contents)

if __name__ == "__main__":
    main()