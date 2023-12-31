from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post  # 매번 지정해줘야 함
    # template_name: '<모델명>_list.html'을 기본값으로 가짐, 기본값과 동일해서 삭제 가능
    context_object_name = 'posts'
    ordering = ['-dt_created']  # 최근에 작성된 게시글이 위로
    paginate_by = 6 # 페이지네이션
    # page_kwarg: 기본값이 'page'이기 때문에 지워도 무방
    # # 현재 페이지를 쿼리 스트링에 어떤 값으로 조회하는지 알려줌

class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html'
    # pk_url_kwarg = 'post_id'  # 기본값 pk
    # context_object_name = 'post'  -> 기본값 사용 중, 삭제 가능
    ## 조회한 데이터를 context로 넘겨줄 때 사용
    

class PostCreateView(CreateView):
    model = Post  # Post 모델을 다룸
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})
        # reverse: url name으로부터 거슬러 올라가서 url을 찾음
        # kwargs(keyword arguments): 사전형으로 키워드를 전달할 때 사용
        # self.object: 새로 생성된 post 객체에 접근

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  # 수정할 때 user의 입력을 받아야 하기 때문에 form 사용
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id'
    
    # 데이터 유효성 검증이 통과되면 이동할 url
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html' -> 기본값과 동일
    # pk_url_kwarg = 'post_id' # 데이터 조회, 존재하지 않으면 404에러 발생
    # context_object_name = 'post' # 존재하면 context에 담아서 전달

    def get_success_url(self):
        return reverse('post-list')

class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'
    # redirect 할 패턴의 이름을 지정