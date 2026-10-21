import string

text = input("Enter text: ")

chars_with_spaces = len(text)
chars_without_spaces = len(text.replace(" ", ""))

sentences = text.count(".") + text.count("!") + text.count("?")

clean_text = text.translate(str.maketrans("", "", string.punctuation))
clean_text = clean_text.lower()

words = clean_text.split()

word_count = len(words)

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

max_count = max(word_freq.values(), default=0)

most_common = []
for word, count in word_freq.items():
    if count == max_count:
        most_common.append(word)

print("Text statistics:")
print("Characters (including spaces):", chars_with_spaces)
print("Characters (excluding spaces):", chars_without_spaces)
print("Word count:", word_count)
print("Sentence count:", sentences)
print("Longest word:", longest_word)
print("Most frequent word:", ", ".join(most_common))