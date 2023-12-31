from .models import Post

def validate_post():
    # 1. 모든 포스트 데이터 가져오기
    posts = Post.objects.all()
    # 2. 각각의 포스트 데이터를 보면서 내용 안에 &가 있는지 체크하기
    for post in posts:
        if '&' in post.content:
            print(post.id, '본 글에 "&"가 있습니다.')
    # 3. 만약 &가 있다면 해당 &를 삭제처리
            post.content = post.content.replace('&', '')
    # 4. 데이터 저장하기
            post.save()
        if post.dt_modified < post.dt_created: # 생성일 이전에 수정일이 있다면
            print(post.id, '본 글의 수정일이 생성일보다 과거입니다')
            post.save() # 포스트를 다시 저장하기 때문에 현재 날짜 기준으로 저장됨