import re


class GrammarChecker:
    def __init__(self):
        self.rules = self.load_grammar_rules()

    def check_subject_verb_agreement(self, groups):
        """
        Check if the subject and verb agree
        groups[0]: subject (මම, අපි, etc.)
        groups[1]: verb
        """
        subject = groups[0]
        verb = groups[1]

        # Check agreement and return tuple of (is_valid, specific_error_message)
        if subject == 'මම':
            is_valid = verb.endswith('මි') or verb.endswith('නවා')
            error_msg = f"'මම' නිවැරදි ක්‍රියා පද අවසානය 'මි' විය යුතුය"
            return is_valid, error_msg
        elif subject == 'අපි':
            is_valid = verb.endswith('මු') or verb.endswith('නවා')
            error_msg = f"'අපි' නිවැරදි ක්‍රියා පද අවසානය 'මු' විය යුතුය"
            return is_valid, error_msg
        elif subject in ['ඔහු', 'ඇය']:
            is_valid = verb.endswith('යි') or verb.endswith('නවා')
            error_msg = f"'{subject}' නිවැරදි ක්‍රියා පද අවසානය 'යි' විය යුතුය"
            return is_valid, error_msg

        return True, ""  # Default case

    def load_grammar_rules(self):
        """Load Sinhala grammar rules"""
        return [
            {
                'name': 'subject_verb_agreement',
                'pattern': r'(මම|අපි|ඔහු|ඇය)\s+(\w+)',
                'check': self.check_subject_verb_agreement
            }
        ]

    def check_sentence(self, sentence):
        """Check grammar rules in a sentence"""
        errors = []
        for rule in self.rules:
            matches = re.finditer(rule['pattern'], sentence)
            for match in matches:
                is_valid, error_msg = rule['check'](match.groups())
                if not is_valid:
                    errors.append({
                        'rule': rule['name'],
                        'position': match.span(),
                        'text': match.group(),
                        'message': error_msg
                    })
        return errors
