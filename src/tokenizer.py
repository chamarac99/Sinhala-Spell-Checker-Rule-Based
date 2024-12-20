import re

class SinhalaTokenizer:
    def _init_(self):
        # Define Sinhala word boundaries
        self.word_pattern = r'[\u0D80-\u0DFF]+'
        
    def tokenize(self, text):
        """Split text into Sinhala words"""
        words = re.findall(self.word_pattern, text)
        return words
