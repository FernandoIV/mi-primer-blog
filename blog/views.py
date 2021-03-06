from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.
def post_list(request):
	posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def post_nuevo(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.fecha_publicacion = timezone.now()
			post.save()
			return redirect('blog:post_detail',pk=post.pk)
	else:
		form = PostForm()
	return render(request,'blog/post_editar.html',{'form':form})

def post_editar(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit = False)
			post.autor = request.user
			post.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_editar.html',{'form':form})