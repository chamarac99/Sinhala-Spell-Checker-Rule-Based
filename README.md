# Sinhala Spelling and Grammar Checker

This project is a **Sinhala Spelling and Grammar Checker** implemented in Python, featuring a **Streamlit web interface**. It uses custom modules for tokenization, dictionary-based spelling checking, and grammar rule analysis.

---

## Features

- **Spell Checking:** Identifies misspelled words and provides suggestions.
- **Grammar Checking:** Detects grammatical issues in Sinhala sentences.
- **Streamlit Interface:** User-friendly web interface for text input and result visualization.
- **Customizable Corpus:** Supports a user-defined text corpus for dictionary loading.
# Setup Instructions

## Prerequisites

- Python 3.8+
- Virtual Environment (optional but recommended)

---

## Setup

### Virtual Environment
1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
2. **Activate the virtual environment**:
    - On Linux/Mac:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

### Install Dependencies
- install Streamlit:
    ```bash
    pip install streamlit
    ```

---

## Usage

### Run the Streamlit App
1. Use the following command to launch the app:
    ```bash
    streamlit run interface.py
    ```
2. The app will open in your default web browser.

### Interacting with the App
- **Input Text**: Enter Sinhala text in the provided text area.
- **Check Spelling and Grammar**: Click the "Check Text" button to analyze the input.
- **View Results**: The app will display:
  - Spelling errors with suggestions.
  - Grammar issues, if any.

---

## Customization

### Dictionary Corpus
- Add or modify text files in the `data/` folder to enhance the dictionary's word base.

### Extend Functionality
- Modify or add modules in the `src/` directory to improve or extend features.

---

## Development

### Running Core Logic
- Execute the core logic without the Streamlit interface:
    ```bash
    python main.py
    ```

### Running Tests
1. Add test cases to the `tests/` directory.
2. Execute tests using:
    ```bash
    pytest tests/
    ```

---

## Future Enhancements
- Add more advanced grammar rules.
- Implement real-time tokenization and analysis.
- Extend the Streamlit interface to support batch text processing.

---

## License
This project is open-source. Feel free to modify and distribute it.

---

## Author
**Chamara Bandara**  
Computer Engineering Undergraduate, University of Jaffna
