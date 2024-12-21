import os


class SinhalaDictionary:
    def _init_(self):
        self.words = {}
        self.word_frequency = {}

    def tokenize(self, text):
        """Split text into words"""
        return text.replace('.', ' ').split()

    def add_word(self, word):
        """Add a word to the dictionary"""
        if word in self.words:
            self.word_frequency[word] += 1
        else:
            self.words[word] = set([word])
            self.word_frequency[word] = 1

    def load_from_corpus(self, data):
        """Load words from multiple text files in a folder"""
        # Get list of all text files in the data folder
        txt_files = [f for f in os.listdir(data) if f.endswith('.txt')]

        # Process each file
        for file_name in txt_files:
            file_path = os.path.join(data, file_name)


            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    words = self.tokenize(text)
                    for word in words:
                        self.add_word(word)
            except Exception as e:
                print(f"Error processing file {file_name}: {str(e)}")

    def get_word_frequency(self, word):
        """Get how many times a word appears in the corpus"""
        return self.word_frequency.get(word, 0)

    def print_statistics(self):
        """Print dictionary statistics"""
        print("\nDictionary Statistics:")
        print(f"Total unique words: {len(self.words)}")
        print(f"Top 10 most frequent words:")
        sorted_words = sorted(self.word_frequency.items(), key=lambda x: x[1], reverse=True)
        for word, freq in sorted_words[:10]:
            print(f"'{word}': {freq} times")
