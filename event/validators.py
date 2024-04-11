from django.core.exceptions import ValidationError

import xml.etree.cElementTree as et


def is_svg(filename):
    if filename[:-3] != 'svg':
        return True
    return False


def validate_svg(file):
    if not is_svg(file.name):
        raise ValidationError("File not svg")
