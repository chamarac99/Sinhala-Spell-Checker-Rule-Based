# Streamlit Interface
import streamlit as st
from src.dictionary import SinhalaDictionary
from src.tokenizer import SinhalaTokenizer
from src.spelling_checker import SpellingChecker
from src.grammar_checker import GrammarChecker

def main():
    st.title("Sinhala Spelling and Grammar Checker")

    # Input text
    text = st.text_area("Enter Sinhala text for checking:", height=200)

    if st.button("Check Text"):
        if text.strip():
            st.write("## Results")

            # Initialize components
            dictionary = SinhalaDictionary()
            dictionary.load_from_corpus("data")
            tokenizer = SinhalaTokenizer()
            spelling_checker = SpellingChecker(dictionary)
            grammar_checker = GrammarChecker()

            # Check spelling
            st.subheader("Spelling Errors")
            words = tokenizer.tokenize(text)
            spelling_errors = []
            for word in words:
                is_correct, suggestions = spelling_checker.check_word(word)
                if not is_correct:
                    spelling_errors.append((word, suggestions))

            if spelling_errors:
                for word, suggestions in spelling_errors:
                    st.write(f"- **Word**: `{word}`")
                    st.write(f"  Suggestions: {', '.join(suggestions)}")
            else:
                st.write("No spelling errors found.")

            # Check grammar
            st.subheader("Grammar Errors")
            sentences = tokenizer.sentence_tokenize(text)
            grammar_errors_found = False

            for sentence in sentences:
                grammar_errors = grammar_checker.check_sentence(sentence)
                if grammar_errors:
                    grammar_errors_found = True
                    st.write(f"- **Sentence**: `{sentence}`")
                    for error in grammar_errors:
                        st.write(f"  - {error['message']}")

            if not grammar_errors_found:
                st.write("No grammar errors found.")
        else:
            st.error("Please enter some text to check.")

if __name__ == "__main__":
    main()
