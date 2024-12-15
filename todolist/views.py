from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    query = request.GET.get('q')  
    if query:
        todos = Todo.objects.filter(title__icontains=query).order_by('-created_at')  # Filter todos batay sa search query
    else:
        todos = Todo.objects.all().order_by('-created_at')
    message = "No matching todos found." if query and not todos else None
    return render(request, 'todo_list.html', {'todos': todos, 'query': query, 'message': message})



def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})