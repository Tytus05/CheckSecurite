import pytest
from main import (
    HasNumberValidator,
    HasSpecialCharactersValidator,
    HasUpperCharactersValidator,
    HasLowerChracterValidator,
    LenghtValidator,
    HaveIbeenPwndValidator,
    ValidationErorr
    )


def test_if_has_number_validator_positive():
    # given
    valdator = HasNumberValidator('Barbra1')
    # when
    result = valdator.is_valid()
    # then
    assert result is True


def test_if_has_number_validator_negative():
    # given
    validator = HasNumberValidator('Barbra')
    # when
    with pytest.raises(ValidationErorr) as error:
        validator.is_valid()
        assert '-- Hasło musi miec licze' in str(error.value)
 


def test_if_has_special_characters_validator_positive():
    # given
    valdator = HasSpecialCharactersValidator('barbra1@')
    # when
    result = valdator.is_valid()
    # then
    assert result is True

def test_if_has_special_characters_validator_negative():
    # given
    validator = HasSpecialCharactersValidator('barbra1')
    #when
    with pytest.raises(ValidationErorr) as error:
        validator.is_valid()
        assert '-- Hasło musi miec specjalny znak' in str(error.value)

def test_if_has_upper_characters_validator_positive():
    # given
    valdator = HasUpperCharactersValidator('Barbra1@')
    # when
    result = valdator.is_valid()
    # then
    assert result is True

def test_if_has_upper_characters_validator_negative():
    # given
    validator = HasUpperCharactersValidator('barbra1@')
    # when
    with pytest.raises(ValidationErorr) as error:
        validator.is_valid()
        assert '-- Haslo musi miec duza litere' in str(error.value)
   

def test_if_has_lower_characters_validator_positive():
    # given
    valdator = HasLowerChracterValidator('Barbra1@')
    # when
    result = valdator.is_valid()
    # then
    assert result is True

def test_if_has_lower_characters_validator_negatiwe():
    # given
    validator = HasLowerChracterValidator('BARBARA1@')
    # when
    with pytest.raises(ValidationErorr) as error:
        validator.is_valid()
        assert '-- Haslo musi miec mala litere' in str(error.value)
   

def test_if_lenght_validator_positive():
    # given
    valdator = LenghtValidator('Barbrat1@')
    # when
    result = valdator.is_valid()
    # then
    assert result is True

def test_if_lenght_validator_negative():
    # given
    validator = LenghtValidator('Bara1@')
    # when
    with pytest.raises(ValidationErorr) as error:
        validator.is_valid()
        assert '-- Haslo musi miec 8 znakow' in str(error.value)

# def test_have_i_been_pwnd_validator_positive(requests_mock):
#     data = '700BB1CFFB6C5629E0E6A3AB5017CDB7246:10\r\nFE77571DE78CA26B2FB06CD64F65A5B8F07:1'
#     requests_mock.get('https://api.pwnedpasswords.com/range/A63CC', text=data)
#     validator = HaveIbeenPwndValidator('Jan23!')
#     assert validator.is_valid() is False


# def test_have_i_been_pwnd_validator_negative(requests_mock):
# #     #FE77571DE78CA26B2FB06CD64F65A5B8F07
# #     #'Jan23!'
# #     #A63CC 693BB1CFFB6C5629E0E6A3AB5017CDB7246
#     data = '693BB1CFFB6C5629E0E6A3AB5017CDB7246:10\r\nFE77571DE78CA26B2FB06CD64F65A5B8F07:1'
#     requests_mock.get('https://api.pwnedpasswords.com/range/A63CC', text=data)
#     validator = HaveIbeenPwndValidator('Jan23!')
#     assert validator.is_valid() is False

# # def test_have_i_been_pwnd_validator_negative():
   
    
# #     validator = HaveIbeenPwndValidator('test')
# #     assert validator.is_valid() is True



