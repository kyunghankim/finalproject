from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def predict(request):

    return render(request, 'prediction_views/predict.html')


def intro(request):
    
    return render(request, 'prediction_views/intro.html')

def notice(request):
    
    return render(request, 'prediction_views/notice.html')

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'prediction_views/index.html', context)

def new(request):
    #POST로 들어온 경우(method가)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('prediction_views:detail', article.pk)
    else:
        #작성 양식 보여주기(여기서 작성)
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'prediction_views/new.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    comment_form = CommentForm()

    context = {
        'article': article,
        'comment_form': comment_form,
        # 'image': image,
    }
    return render(request, 'prediction_views/detail.html', context)

def delete(request, pk): # POST 
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
    return redirect('prediction_views:index')

def edit(request, pk):
    # 1. Database에서 data 가져오기
    # else에 있던 코드를 그대로 복사
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        # data 수정!
         
        form = ArticleForm(request.POST, instance=article)
                 
        if form.is_valid():
             
            article = form.save()
             
            return redirect('prediction_views:detail',article.pk)
    # GET
    else:
         
        form = ArticleForm(instance=article)
         
    context = {
        'form': form,
    }
    return render(request, 'prediction_views/edit.html', context)

def like(request,pk):
    user = request.user
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # 1.
        if user in article.like_users.all() :
            article.like_users.remove(user)
        else:
            article.like_users.add(user)
        
    return redirect('prediction_views:detail', pk)

def comments_new(request, article_pk): #POST
    # 1. 요청이 POST인지 점검
    if request.method == 'POST':
        # 2. form에 data를 집어넣기(목적==유효성 검사)
        # request.POST => {'content':'와댓글'}
        form = CommentForm(request.POST)
        # 3. 유효성 검사 시행
        if form.is_valid():
            # 4. database에 저장
            comment = form.save(commit=False) #<-
            # 4-1. article 정보 주입
            comment.article_id = article_pk
            comment.save()
        request.POST
    # 5. 생성된 댓글 확인할 수 있는 곳으로 안내
    return redirect('prediction_views:detail', article_pk)

def comments_delete(request, article_pk, pk): # POST
    # 0. 요청이 POST인지 점검
    if request.method == 'POST':
        # 1. pk를 가지고 삭제하려는 data 꺼내오기
        comment = Comment.objects.get(pk=pk)
        # 2. 삭제
        comment.delete()
    # 3. 삭제되었는지 확인 가능한 곳으로 안내
    return redirect('prediction_views:detail', article_pk)

def comments_edit(request, article_pk, pk): #<- GET,POST
    # 0-0. Database에서 수정하려 하는 data 가져오기
    comment = Comment.objects.get(pk=pk)
    # 0. 요청 종류 POST/GET 확인
    if request.method == 'POST':
        #실제로 수정!
        # 1. form에 '넘어온 data' & '수정하려는 data' 집어넣기 
        form = CommentForm(request.POST, instance=comment)
        # 2. 유효성 검사
        if form.is_valid():
        # 3. 검사를 통과했다면, save
            comment = form.save()
        # 4. 변경된 결과 확인하는 곳으로 안내
        return redirect('prediction_views:detail', article_pk)
        
    else:

        form = CommentForm(instance=comment)

    context = {
        'form': form, 
    }
    return render(request, 'prediction_views/comments_edit.html', context)