from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.

class Post(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50, unique=True, error_messages = {'unique': '이미 존재하는 제목입니다.'})
    content = models.TextField(validators=
                               [MinLengthValidator(10, '10자 이상 적어주세요.'), validate_symbols])
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    
    def __str__(self):
        return self.title