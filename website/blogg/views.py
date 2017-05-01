from __future__ import unicode_literals
from blogg.models import Post
from blogg.models import Mate
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView



class Home(TemplateView):
	template_name = 'blogg/index.html'


class Lists(ListView):
	template_name = 'blogg/post.html'
	model = Post


class Detail(DetailView):
	template_name = 'blogg/detail.html'
	model = Post


class List(ListView):
	template_name = 'blogg/new.html'
	model = Mate

class Details(DetailView):
	template_name = 'blogg/details.html'
	model = Mate



# Create your views here.
#def home(request):
#	helloworld="helloworld"
#	return render(request, 'blogg/index.html', {'helloworld' :helloworld})
