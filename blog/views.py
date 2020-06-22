from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.views.generic import ListView , UpdateView , DetailView , DeleteView, CreateView 
from .mixins import LoginRequiredMixin , UserPassesTestMixin 
from .models import Post
from django.contrib.auth.models import User
from .forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect , render ,reverse
from django.template.loader import get_template
from django.views.generic.edit import FormMixin
from .forms import CommentForm


def home(request):
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5




class PostDetailView(FormMixin,DetailView):
    model = Post
    template_name='blog/detail.html'
    context_object_name ='post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','tech','links']
    template_name='blog/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


  
class TechPostListView(ListView):
    model = Post
    template_name = 'blog/tech.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(tech=self.kwargs.get('tech')).order_by('-date_posted')




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'tech','content','links']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name='blog/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')








def about(request):
    return render(request,'blog/about.html')




# new imports that go at the top of the file

def contact(request):
    form_class = ContactForm


    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('blog/contact_template.html')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                contact_email,
                ['pythonblog.gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('blog-home')

    return render(request, 'blog/contact.html', {
        'form': form_class,
    })