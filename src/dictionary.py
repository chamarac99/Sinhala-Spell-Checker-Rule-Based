class SinhalaDictionary:
    def __init__(self):
        self.words = {}
        self.word_frequency = {}

    def load_from_corpus(self, corpus_path):
        with open(corpus_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = self.tokenize(text)
            for word in words:
                self.add_word(word)