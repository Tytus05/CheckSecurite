"""Collection of password validators"""
from abc import ABC, abstractmethod
from string import ascii_uppercase, ascii_lowercase, punctuation
from hashlib import sha1
from requests import get


class ValidationErorr(Exception):
    """Exception for validation error"""


class Validator(ABC):
    """Interfence for validator"""
    @abstractmethod
    def __init__(self,text):
        """Force to implement __init__method"""  
    @abstractmethod
    def is_valid(self):
        """Force to implement is_valid method"""


class LenghtValidator(Validator):
    """Validator that checks if password is long enaugh"""
    def __init__(self,text):
        self.text = text
    def is_valid(self):
        """Checks if text is valid
        Raises:

            ValidationErorr: text is not valid because it is too short 
        Returns:
            bool: text in long enough
        """
        if len(self.text) >= 8:
            return True

        raise ValidationErorr('-- Haslo musi miec 8 znakow')


class HasNumberValidator(Validator):
    """Interface for validators"""
    def __init__(self,text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationErorr: text is not valid because there is no number in text

        Returns:
            bool: has number in text
        """
        numbers = []
        for number in range(11):
            if str(number) in self.text:
                numbers.append(number)
        if len(numbers)>0:
            return True

        raise ValidationErorr('-- Haslo musi miec licze')


class HasSpecialCharactersValidator(Validator):
    """Validator that checks if number appears in text"""
    def __init__(self,text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationErorr: text is not valid because there is no special character in text

        Returns:
            bool: has special character in text
        """
        specials = []
        for special in punctuation:
            if special in self.text:
                specials.append(special)
        if len(specials)>0:
            return True

        raise ValidationErorr('-- Haslo musi miec specjalny znak')


class HasUpperCharactersValidator(Validator):
    """Validator that checks if upper characters appears in text"""
    def __init__(self,text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationErorr: text is not valid because there is no upper leatter in text

        Returns:
            bool: has upper leatter in text
        """
        uppers = []
        for upper in ascii_uppercase:
            if upper in self.text:
                uppers.append(upper)
        if len(uppers)>0:
            return True

        raise ValidationErorr('-- Hasło musi miec duza litere')


class HasLowerChracterValidator(Validator):
    """Validator that checks if lower characters appears in text"""
    def __init__(self,text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationErorr: text is not valid because there is no lower leatter in text

        Returns:
            bool: has lower leatter in text
        """
        lowers = []
        for lower in ascii_lowercase:
            if lower in self.text:
                lowers.append(lower)
        if len(lowers)>0:
            return True

        raise ValidationErorr('-- Hasło musi miec mala litere')


class HaveIbeenPwndValidator(Validator):
    """Validator that checks if password is safe """
    def __init__(self,text):
        self.text = text
        self.password = password
        self.big_has_word = None
        self.rest_big_has_word = None
        self.first_five_numbers = None
        self.has_passowrd_api = None

    def is_valid(self):
        """Checks if password is leaked

        Raises:
            ValidationErorr: password is not valid because it is present in some leak 

        Returns:
            bool: password is safe 
        """
    #hasz
        has_word_byte = sha1(self.password.encode('utf-8'))
        has_word =has_word_byte.hexdigest()
        self.big_has_word = has_word.upper()
        # return self.big_has_word

    #first_five_passord_numbers
        self.first_five_numbers = self.big_has_word[:5]
        # return self.first_five_numbers

    #check_API
        jon = get('https://api.pwnedpasswords.com/range/'+ self.first_five_numbers)
        self.has_passowrd_api = jon.text

    #last_password_numbers
        self.rest_big_has_word = self.big_has_word[5:]

    #check_password
        if self.rest_big_has_word in self.has_passowrd_api:
            return False

        return True

class PasswordValidator(Validator):
    """Validator that checks if password is corect"""
    def __init__(self,password):
        self.password = password
        self.validators = [
            LenghtValidator,
            HasNumberValidator,
            HasSpecialCharactersValidator,
            HasUpperCharactersValidator,
            HasLowerChracterValidator,
            HaveIbeenPwndValidator,
        ]
    def is_valid(self):
        """Checks if password is valid

        Returns:
            bool: returns true if password passed all requirements
        """
        corect = []
        for clas_name in self.validators:
            one_valid = clas_name(self.password)
            corect.append(one_valid.is_valid())
        if all(corect):
            return True

        return False

def load_end_encoding_password():
    list_password = []
    with open ('Password.txt',mode='r', encoding='utf-8') as file_one:
        for password_one in file_one:
            list_password.append(password_one.strip())
        return list_password

for password in load_end_encoding_password():
    try:
        first_password = PasswordValidator(password)
        if first_password.is_valid():
            print(f'{password} -- Hasło silne i bezpieczne')
            with open('Password_safe.txt',mode='a',encoding='utf-8') as file:
                file.write(f"{password}\n")
    except ValidationErorr as error:
        print(password, error)
