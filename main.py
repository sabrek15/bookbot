def count_words(text):
    print(len(text.split()))

def count_characters(text):

    text = text.lower()
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    count_words(file_contents)

    char_counts = count_characters(file_contents)

    for char, count in char_counts.items():
        print(f"'{char}': {count}")
    
    # print(file_contents)

if __name__ == "__main__":
    main()