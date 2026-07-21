from word_counter import WordCounter

print("===== WORD COUNT TOOL =====\n")

text = input("Enter a sentence or paragraph:\n\n")

counter = WordCounter(text)

print("\n===== RESULT =====")
print(f"Words      : {counter.count_words()}")
print(f"Characters : {counter.count_characters()}")
print(f"Sentences  : {counter.count_sentences()}")

print("\nWord Frequency:")

for word, count in counter.word_frequency().items():
    print(f"{word} : {count}")