from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse, HttpResponse
from core.models import Book, Author
from django.contrib import messages
from .forms import BookAddForm,AuthorAddForm
from http import HTTPStatus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    def get(self, request):
        context = {
            "title": "Book",
            "book_list": Book.objects.all(),
            "form":BookAddForm()
        }
        return render(request, self.template_name, context)

#.............................................................................
# Book View
#.............................................................................


class BookView(TemplateView):
    template_name = "book_list.html"

    def get(self, request):
        book_list = Book.objects.all().order_by("-created_at")
        page = request.GET.get('page', 1)
        paginator = Paginator(book_list, 5)
        try:
            book_list = paginator.page(page)
        except PageNotAnInteger:
            book_list = paginator.page(1)
        except EmptyPage:
            book_list = paginator.page(paginator.num_pages)

        context = {
            "book_active":"active",
            "title": "Author",
            "book_list": book_list,
            "form":BookAddForm()
        }
        return render(request, self.template_name, context)
    
    def post(self,request):
        get_id = request.POST.get('get_project_id')
        if get_id:
            project_obj = get_object_or_404(Book, pk=get_id)
            if project_obj:
                form = BookAddForm(request.POST, instance=project_obj)
                if form.is_valid():
                    form.save()
                    response = {
                        'status': 'updated',
                        'ok': True
                    }
                    return JsonResponse(response)
        response = {
            'status': 'Error while updating',
            'ok': False,
            'errors':form.errors
        }
        return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)


class BookCreateView(TemplateView):
    model = Book
    form_class = BookAddForm

    def get(self, request):
        get_id = request.GET.get('get_id')
        project_obj = Book.objects.get(id=get_id)
        form = BookAddForm(instance=project_obj)
        return HttpResponse(form.as_p())
    def post(self, request):
        create_form = BookAddForm(request.POST)
        if create_form.is_valid():
            ob = create_form.save(request)
            messages.success(request, "Created {0} Book successfully".format(ob.title))
            return redirect('/book-list')


def book_delete_view(request, pk):
    Book.objects.get(pk=pk).delete()
    messages.success(request, "Created {0} Book successfully".format(pk))
    return redirect('/book-list')

#.............................................................................
# Author View
#.............................................................................

class AuthorView(TemplateView):
    template_name = "author_list.html"
    def get(self, request):
        author_list = Author.objects.all().order_by("-created_at")
        page = request.GET.get('page', 1)
        paginator = Paginator(author_list, 5)
        try:
            author_list = paginator.page(page)
        except PageNotAnInteger:
            author_list = paginator.page(1)
        except EmptyPage:
            author_list = paginator.page(paginator.num_pages)

        context = {
            "author_active":"active",
            "title": "Author",
            "author_list": author_list,
            "form":AuthorAddForm()
        }
        return render(request, self.template_name, context)

    def post(self,request):
        get_id = request.POST.get('get_project_id')
        if get_id:
            project_obj = get_object_or_404(Author, pk=get_id)
            if project_obj:
                form = AuthorAddForm(request.POST, instance=project_obj)
                if form.is_valid():
                    form.save()
                    response = {
                        'status': 'updated',
                        'ok': True
                    }
                    return JsonResponse(response)
        response = {
            'status': 'Error while updating',
            'ok': False,
            'errors':form.errors
        }
        return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)


class AuthorCreateView(TemplateView):
    model = Author
    form_class = AuthorAddForm

    def get(self, request):
        get_id = request.GET.get('get_id')
        project_obj = Author.objects.get(id=get_id)
        form = AuthorAddForm(instance=project_obj)
        return HttpResponse(form.as_p())
        
    def post(self, request):
        create_form = AuthorAddForm(request.POST)
        if create_form.is_valid():
            ob = create_form.save(request)
            messages.success(request, "Created {0} Book successfully".format(ob.email))
            return redirect('/author-list')
            

def author_delete_view(request, pk):
    Author.objects.get(pk=pk).delete()
    messages.success(request, "Created {0} Book successfully".format(pk))
    return redirect('/author-list')