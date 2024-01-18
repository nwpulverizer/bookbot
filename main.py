def main():
    def get_text(file):
        with open(file, "r") as f:
            file_contents = f.read()
        return file_contents

    def count_words(book_text):
        length = len(book_text.split())
        return length

    def count_chars(book_text):
        words = book_text.split()
        characters = {}
        for word in words:
            for char in word.lower():
                characters[char] = characters.get(char, 0) + 1
        return characters

    def create_report(book_file):
        start = f"--- Begin report of {book_file} ---"
        text = get_text(book_file)
        words = count_words(text)
        chars = count_chars(text)
        alphas = {k: v for k, v in chars.items() if k.isalpha()}
        sorted_by_count = sorted(alphas.items(), key=lambda kv: kv[1], reverse=True)

        print(start)
        print(f"{words} words found in the document \n")
        for pair in sorted_by_count:
            print(f"The '{pair[0]}' character was found {pair[1]} times")
        print("--- End report ---")

    book_path = "./books/frankenstein.txt"
    create_report(book_path)


main()
