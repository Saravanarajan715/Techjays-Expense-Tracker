import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_uppercase',
            )
        
        
        if not re.search(r'[@$!%*?&#]', password):
            raise ValidationError(
                _("The password must contain at least one special character."),
                code='password_no_special',
            )

        
        if len(password) < 8:
            raise ValidationError(
                _("The password must be at least 8 characters long."),
                code='password_too_short',
            )

    def get_help_text(self):
        return _(
            "Your password must be at least 8 characters long, contain at least one uppercase letter, and one special character."
        )
