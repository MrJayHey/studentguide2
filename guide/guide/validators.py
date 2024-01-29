import re
from django.core.exceptions import ValidationError

class SymbolValidator:
    def __init__(self, symbols='&^%$#'):
        self.symbols = symbols

    def validate(self, password, user=None):
        if any(char in self.symbols for char in password):
            raise ValidationError(
                'Your password can\'t contain the following symbols: %s' % self.symbols,
                code='password_contains_symbols',
            )

    def get_help_text(self):
        return 'Your password can\'t contain the following symbols: %s' % self.symbols
