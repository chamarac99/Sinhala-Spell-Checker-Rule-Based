from src.dictionary import SinhalaDictionary
from src.tokenizer import SinhalaTokenizer
from src.spelling_checker import SpellingChecker
from src.grammar_checker import GrammarChecker

def main():
    # Initialize components
    dictionary = SinhalaDictionary()
    tokenizer = SinhalaTokenizer()
    spelling_checker = SpellingChecker(dictionary)
    grammar_checker = GrammarChecker()
    
    # Example usage
    text = "මම ගෙදර යනවා"
    words = tokenizer.tokenize(text)
    
    # Check spelling
    for word in words:
        is_correct, suggestions = spelling_checker.check_word(word)
        if not is_correct:
            print(f"Spelling error in word: {word}")
            print(f"Suggestions: {suggestions}")

if _name_ == "_main_":
    main()
