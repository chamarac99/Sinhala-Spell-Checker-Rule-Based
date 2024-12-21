import re


class SinhalaTokenizer:
    def _init_(self):
        # Define Sinhala word boundaries
        self.word_pattern = r'[\u0D80-\u0DFF]+'

    def tokenize(self, text):
        """Split text into Sinhala words"""
        words = text.replace('.', ' ').split()
        return words


    def sentence_tokenize(self, text):
        """Split text into sentences"""
        # Basic sentence splitting on Sinhala full stop
        sentences = text.split('.')
        return [s.strip() for s in sentences if s.strip()]
