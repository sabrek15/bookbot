def count_words(text):
    print(len(text.split()))

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    count_words(file_contents)
    # print(file_contents)

if __name__ == "__main__":
    main()