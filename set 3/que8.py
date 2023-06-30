def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        word_count = len(text.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Example input
input_file = "input.txt"
output_file = "output.txt"

count_words(input_file, output_file)
