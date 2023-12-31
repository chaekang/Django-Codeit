from django.core.exceptions import ValidationError

def validation_no_hash(value):
    if '#' in value:
        raise ValidationError('"#"를 사용할 수 없습니다.')
    
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('숫자를 사용할 수 없습니다.')
        
def validate_score(value):
    if (value < 0) or (value > 10):
        raise ValidationError('0에서 10 사이의 숫자를 입력해주세요.')