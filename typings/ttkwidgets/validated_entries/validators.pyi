"""
This type stub file was generated by pyright.
"""

"""
Author: Dogeek
License: GNU GPLv3
Source: This repository

Validators to validate entry input.
"""
class Validator:
    """
    Base validator class

    Specify the VALIDATE_ON class attribute (defaults to 'all') to change
    on which tkinter condition the validation will be done.

    Possibilities are :
        * 'all'
        * 'none'
        * 'focus'
        * 'focusin'
        * 'focusout'
        * 'key'
    """
    VALIDATE_ON = ...
    def __init__(self, validate_on=...) -> None:
        ...
    
    def validate(self, widget): # -> dict[str, Any | str | tuple[Any, Literal['%P']]]:
        ...
    
    @property
    def is_valid(self): # -> bool:
        ...
    


class MultiValidator:
    """
    Base class to handle multiple validators attachment.
    """
    def __init__(self, *validators, validate_on=...) -> None:
        """
        :param *validators: Validator instances or classes to attach
        :param validate_on: tkinter condition on which the validation will be done
                            default : 'all', see `help(Validator)` for a list of
                            possible values
        """
        ...
    
    def validate(self, widget): # -> dict[str, str | tuple[Any, Literal['%P']]]:
        ...
    
    @property
    def is_valid(self):
        ...
    


class AnyValidator(MultiValidator):
    """
    Validates any attached validators. The input will be deemed valid if and only if
    one of the attached validators deem the value valid.
    """
    ...


class AllValidator(MultiValidator):
    """
    Validates all attached validators. The input will be deemed valid if and only if
    all attached validators deem the value valid.
    """
    ...


class RegexValidator(Validator):
    """
    A validator that will check against a regular expression stored in the REGEX
    class attribute

    REGEX can either be a re.Pattern or a python string.
    """
    REGEX = ...
    def __init__(self, regex=..., **kwargs) -> None:
        ...
    


class IntValidator(Validator):
    ...


class FloatValidator(RegexValidator):
    REGEX = ...


class PercentValidator(Validator):
    ...


class StringValidator(Validator):
    """
    A validator you have to instanciate with a string containing the
    characters you want in.
    """
    def __init__(self, string) -> None:
        """
        :param string: String of allowed characters
        :type string: str
        """
        ...
    


class CapitalizedStringValidator(RegexValidator):
    REGEX = ...


class EmailValidator(RegexValidator):
    VALIDATE_ON = ...
    REGEX = ...


class PasswordValidator(RegexValidator):
    """
    Password validator. The requirements are as follows :
        * At least 1 lowercase character
        * At least 1 uppercase character
        * At least 1 digit
        * At least 1 special character (!@#$%^&*)
        * Be at least 8 characters long
    """
    VALIDATE_ON = ...
    REGEX = ...


class IPv4Validator(RegexValidator):
    """
    Validates IPv4 addresses. The following are valid:
        * localhost
        * 192.168.0.1
        * localhost:3158
    """
    VALIDATE_ON = ...
    REGEX = ...


