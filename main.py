import sys
from stats import count_words, counter, sort_char_count

# Check for proper usage
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = sys.argv[1]  # This line was missing the assignment
    
    # Get book text
    book_text = get_book_text(path)
    
    # Count words
    word_count = count_words(book_text)
    
    # Count characters
    char_counts = counter(book_text)
            
    # Sort character counts
    sorted_counts = sort_char_count(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for item in sorted_counts:
        char = item["char"]
        count = item["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")  

main()

