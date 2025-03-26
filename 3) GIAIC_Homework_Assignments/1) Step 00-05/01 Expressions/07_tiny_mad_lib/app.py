# Constant for the beginning of the sentence
SENTENCE_START = "Once upon a time, there was a"

# Prompt the user for inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Construct and print the fun sentence
mad_lib_sentence = f"{SENTENCE_START} {adjective} {noun} that loved to {verb}."
print(mad_lib_sentence)