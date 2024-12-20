class SpellingChecker:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        
    def check_word(self, word):
        """Check if a word is spelled correctly"""
        if word in self.dictionary.words:
            return True, []
        
        suggestions = self.get_suggestions(word)
        return False, suggestions
