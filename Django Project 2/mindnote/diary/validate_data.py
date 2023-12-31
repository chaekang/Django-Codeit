from .models import Page
import random

def validate_pages():
# 1. 모든 데이터 불러오기
    pages = Page.objects.all()
# 2. 각각의 포스트 데이터 보면서 score가 0이상 10이하인지 확인
    for page in pages:
        if (page.score < 0) or (page.score > 10):
# 3. 만약 범위를 넘어간다면 score 수정
            page.score = random.randint(0, 10)
# 4. 데이터 저장
            page.save()