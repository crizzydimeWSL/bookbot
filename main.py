import sys
from stats import count_words
from stats import count_char
from stats import sort_char_counts




def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    





def main():
    #book_content = get_book_text('books/frankenstein.txt')
    #num_words = count_words(book_content)
    #print(f"{num_words} words found in the document.")
    #char_counts = count_char(book_content)
    #print(char_counts)

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")


    try:
        book_content = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The File '{filepath}' was not found.")
        sys.exit(1)
    
    num_words = count_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_char(book_content)
    sorted_char_counts = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['character']}: {entry['count']}")

    print("============= END ===============") 


if __name__ == "__main__":
    main()




    