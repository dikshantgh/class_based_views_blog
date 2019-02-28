from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, FormMixin
from blog.models import Post, Comment
from django.shortcuts import get_object_or_404
from blog.forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class PostListView(ListView):
    template_name = 'blog/list_posts.html'
    model_name = Post
    queryset = Post.published.all()
    # by default it is model_list i.e post_list or object_list
    context_object_name = 'post'
    paginate_by = 5


class PostDetailView(SuccessMessageMixin, FormMixin, DetailView):
    template_name = 'blog/detail_posts.html'
    context_object_name = "main_post"
    queryset = Post.published.all()
    model = Comment
    form_class = CommentForm
    success_message = "Your Comment is added successfully"

    def get_object(self):  # Django calls the get_object method which looks for a pk or slug
        return get_object_or_404(Post, slug=self.kwargs['post'], status='p', publish__year=self.kwargs['year'],
                                 publish__month=self.kwargs['month'], publish__day=self.kwargs['day'])

    def get_success_url(self):
        return reverse_lazy('blog:detail_posts', kwargs={'year': self.kwargs['year'], 'month': self.kwargs['month'],
                                                         'day': self.kwargs['day'], 'post': self.kwargs['post']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

    # GET method gets the form while POST methods sends data to server
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class SearchListView(ListView):
	template_name = 'blog/search.html'
	model_name = Post
	context_object_name = "main_post"
	#queryset = Post.published.all()
	paginate_by = 3

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Post.published.filter(Q(title__icontains=query) | Q(body__icontains=query))
		else:
			return Post.published.all()





    # def get(self, request, *args, **kwargs):
    # 	form = CommentForm()
    # 	return render(request,self.template_name,{'form_comment':form})

# class EmailPostView(SuccessMessageMixin,FormView):
# 	template_name = 'blog/share_form.html'
# 	form_class = EmailPostForm
# 	success_message = 'Post Shared in Email successfully'

# 	# for using reverse_lazy with argumnets coming from urls
# 	def get_success_url(self):
# 		return reverse_lazy('blog:post_share', args=[self.kwargs['post_slug']])

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['slug_name'] = self.kwargs['post_slug']
# 		return context

    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    # def form_valid(self, form):
    # 	post = Post.published.get(slug =self.kwargs['post_slug'])
    # 	url_name = "please visit http://127.0.0.1:8000"+str(post.get_absolute_url())
    # 	form.send_email(url_name) # can use this to send to form . in this case to send_email
    # 	return super().form_valid(form)
