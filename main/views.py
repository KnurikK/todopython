from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

def homepage(request):
    return render(request, "test.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")
    
def third(request):
    return HttpResponse("This is page test3")

def details_list(request):
    book_details = Books.objects.all()
    return render(request, "books.html", {"book_details": book_details})

def add_book(request):
    form = request.POST
    text = form["book_text"]
    new_book = Books(text=text)
    new_book.save()
    return HttpResponse("Все работает как надо!")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)
    