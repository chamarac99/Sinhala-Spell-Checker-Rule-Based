class SpellingChecker:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def check_word(self, word):
        """Check if a word is spelled correctly"""
        if word in self.dictionary.words:
            return True, []

        suggestions = self.get_suggestions(word)
        return False, suggestions

    def get_suggestions(self, word):
        """Get spelling suggestions for a misspelled word"""
        suggestions = []

        # 1. Check for similar words using edit distance
        for dict_word in self.dictionary.words:
            if self.levenshtein_distance(word, dict_word) <= 2:
                suggestions.append(dict_word)

        # Sort suggestions by frequency
        suggestions.sort(key=lambda x: self.dictionary.word_frequency.get(x, 0), reverse=True)

        return suggestions[:5]  # Return top 5 suggestions

    def levenshtein_distance(self, s1, s2):
        """Calculate the edit distance between two strings"""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

