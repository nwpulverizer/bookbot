def main():
    def get_text(file):
        with open(file, "r") as f:
            file_contents = f.read()
        return file_contents

    def count_words(book_text):
        length = len(book_text.split())
        print(f"Book has {length} words")
        return length

    frankenstein_text = get_text("books/frankenstein.txt")
    count_words(frankenstein_text)


main()
