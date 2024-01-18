def main():
    with open("./books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    def count_words(book_text):
        length = len(book_text.split())
        return length

    print(count_words(file_contents))


main()
