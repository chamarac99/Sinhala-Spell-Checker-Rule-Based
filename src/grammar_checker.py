import re


class GrammarChecker:
    def __init__(self):
        self.rules = self.load_grammar_rules()

    def load_grammar_rules(self):
        """Load Sinhala grammar rules"""
        return [
            {
                'name': 'subject_verb_agreement',
                'pattern': r'(මම|අපි|ඔහු|ඇය)\s+(\w+)',
                'check': self.check_subject_verb_agreement
            }
        ]
