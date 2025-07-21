from collections import Counter
import re

# 1. Read file
text = open("zen.txt").read().lower()

# 2. Split into words (use re.findall)
words = re.findall(r"\b\w+\b", text)

# 3. Count words
word_counts = Counter(words)

# 4. Count letters (hint: loop over text, keep only isalpha())
letter_counts = Counter(ch for ch in text if ch.isalpha())

# 5. Unique vowel-starting words
vowel_words = {w for w in words if w[0].lower() in "aeiou"}

# 6. Print top 5 of each
print("Top 5 words:", word_counts.most_common(5))
print("Top 5 letters:", letter_counts.most_common(5))
print("Unique vowel words:", sorted(vowel_words))