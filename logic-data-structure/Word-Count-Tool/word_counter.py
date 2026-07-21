class WordCounter:

    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_characters(self):
        return len(self.text)

    def count_sentences(self):
        sentences = self.text.count(".") + self.text.count("!") + self.text.count("?")
        return sentences

    def word_frequency(self):
        frequency = {}

        words = self.text.lower().split()

        for word in words:
            word = word.strip(".,!?;:\"'()[]{}")
            frequency[word] = frequency.get(word, 0) + 1

        return frequency