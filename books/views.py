from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# from django.http import Http404

from .models import Book
from .forms import BookForm, DeleteConfirmForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def show(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    # except Exception:
    #     raise Http404
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/show.html', {'book': book})


def add(request):
    # form = None
    # if request.method == 'POST':
    # name = request.POST.get('name')
    # price = request.POST.get('price')
    # introduction = request.POST.get('introduction')

    # if not name:
    #     pass
    # if not price.isdigit():
    #     pass

    # price = int(price)

    # if price <= 0:
    #     pass

    # if not introduction:
    #     pass

    # Book.objects.create(
    #     name = name,
    #     price = price,
    #     introduction = introduction,
    # )
    form = BookForm(request.POST or None)
    if form.is_valid():
        # Book.objects.create(**form.cleaned_data)
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')

    return render(request, 'books/add.html', {'form': form})


def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')

    return render(request, 'books/edit.html', {'form': form})


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功')
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})
