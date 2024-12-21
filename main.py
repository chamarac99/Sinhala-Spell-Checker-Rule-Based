from src.dictionary import SinhalaDictionary
from src.tokenizer import SinhalaTokenizer
from src.spelling_checker import SpellingChecker
from src.grammar_checker import GrammarChecker


def main():
    # Initialize components
    dictionary = SinhalaDictionary()
    dictionary.load_from_corpus("data")
    tokenizer = SinhalaTokenizer()
    spelling_checker = SpellingChecker(dictionary)
    grammar_checker = GrammarChecker()

    # Example usage
    text = "T20 ජාත්‍යන්තර තරගයකදී කණ්ඩායමක් ලඤණු 7කට දැවී යයි.අයිවරි කෝස්ට් සහ නයිජීරියාව අතර ලේගොස් නවරදී ඊයේ (24) පැවති 20යි 20 තරදයේදී අයිවරි කෝස්ට් කණ්ඩායමේ සිපලුම පිතිකරුවන් ලකුණු 7කට දැවී ගියේය."
    print(f"Checking text: {text}")

    # Check spelling
    words = tokenizer.tokenize(text)
    for word in words:
        is_correct, suggestions = spelling_checker.check_word(word)
        if not is_correct:
            print(f"Spelling error in word: {word}")
            print(f"Suggestions: {suggestions}")

    # Check grammar
    sentences = tokenizer.sentence_tokenize(text)
    grammar_errors = grammar_checker.check_sentence(text)
    if grammar_errors:
        for sentence in sentences:

            grammar_errors = grammar_checker.check_sentence(sentence)
            if grammar_errors:
                print(f"\nGrammar errors found in sentence : {sentence}")
                for error in grammar_errors:

                    print(f"- {error['message']} ")
    else:
        print("\nNo grammar errors found.")


if __name__ == "__main__":
    main()
