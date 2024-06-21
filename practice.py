input_str = "I am Sipra Das"

# Split the input string into words
words = input_str.split()

# Rearrange the order of words and join them with spaces
rearranged_str = ' '.join(words[1:] + [words[0]])

print(rearranged_str)