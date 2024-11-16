# path: views.py
from django.shortcuts import render, redirect
from .models import ToDoListItem
from django.http import HttpResponseRedirect

def todoappView(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request, "todolist.html", {"all_items": all_todo_items})

def addTodoView(request):
    content = request.POST.get("content")
    if content:
        new_item = ToDoListItem(content=content)
        new_item.save()
    return redirect("/todoapp/")

def deleteTodoView(request, item_id):
    item_to_delete = ToDoListItem.objects.filter(id=item_id)
    if item_to_delete.exists():
        item_to_delete.delete()
    return redirect("/todoapp/")

# def