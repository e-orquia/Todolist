from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.utils import timezone



@login_required
def todo_list(request):
    current_time = timezone.localtime(timezone.now())  
    query = request.GET.get('q')  
    if query:
        todos = Todo.objects.filter(title__icontains=query).order_by('-created_at')  
    else:
        todos = Todo.objects.all().order_by('-created_at')
    message = "No matching todos found." if query and not todos else None
    return render(request, 'todo_list.html', {'todos': todos, 'query': query, 'message': message, 'now': current_time})
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        todo.completed = 'completed' in request.POST  
        todo.save()
        if form.is_valid():
            form.save()
        return redirect('todo_list')  
    else:
        form = TodoForm(instance=todo)  

    return render(request, 'todo_form.html', {'form': form, 'todo': todo})





@login_required
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk) 
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})