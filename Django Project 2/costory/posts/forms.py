from django import forms
from.models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content'] # '__all__' 가능
        widgets = {'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': '제목을 입력하세요.'}),
            'content': forms.Textarea(attrs={
                'placeholder': '내용을 입력하세요.'})}
        
    def clean_title(self):
        title = self.cleaned_data['title']  
        # cleaned_data: 폼 필드 작성 시 넣어둔 유효성 검사 통과한 데이터 들어있음
        # 폼 필드 사용하지 않았다면 유효성 검사 통과하지 않은 유저가 작성한 데이터 그대로 들어옴
        # 현재는 model에 유효성 검사가 있기에 cleaned_data에는 유효성 검사 안 한 데이터 있음
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
        return title