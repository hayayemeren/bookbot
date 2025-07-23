from stats import get_num_words, get_num_characters
import sys

def get_book_text(path_to_file):

	with open(path_to_file) as f:
		file_contents = f.read()

	return file_contents


def print_report(text):

	print("============ BOOKBOT ============\n" \
	"Analyzing book found at books/frankenstein.txt...\n"
	"----------- Word Count ----------")
	print(get_num_words(text))
	print("--------- Character Count -------")
	num_characters = get_num_characters(text)
	for i in num_characters:
		print(f"{i["char"]}: {i["num"]}")
	print("============= END ===============")


def main(arg):
	
	if len(arg) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		text = get_book_text(f"../bookbot/{arg[1]}")
		print_report(text)


main(sys.argv)
