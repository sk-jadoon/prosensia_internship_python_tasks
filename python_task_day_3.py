# Take a sentence input from the user
s = input("Enter a sentence: ")

# Split the sentence into a list of words
words_list = s.split()

# Print the list of words
print("List of words : ")
print(words_list)

# Join the list back into a sentence using ' - ' as a separator
joined_sentence = ' - '.join(words_list)

# Print the joined sentence
print("Joined sentence with ' - ' separator : ")
print(joined_sentence)

# Store your first and last name in a tuple
name_tuple = ("Sidra", "Jadoon")
# Print each part using indexing
print("Name from tuple: ")
print("First Name: ", name_tuple[0])
print("Last Name: ", name_tuple[1])
