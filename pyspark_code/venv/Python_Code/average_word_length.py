# Problem description:
# Given a string, calculate the average length of the words in the string.

# Function code:
input_str = "Hello World"
words = input_str.split(" ")
total_length = sum(len(word) for word in words)
average_length = total_length / len(words)

# Function call and print output:
print(average_length)  # Expected output: 5   #5.0

