from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoMod
from .forms import TodoForm

def todo_list(request):
	todo = TodoMod.objects.all()
	return render(request, 'todo/todo_list.html', {'todo': todo})

def todo_new(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('todo_detail', pk=todo.pk)
	else:
		form = TodoForm()
	return render(request, 'todo/todo_edit.html', {'form': form})

def todo_detail(request, pk):
	todo = get_object_or_404(TodoMod, pk=pk)
	return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_edit(request, pk):
	todo = get_object_or_404(TodoMod, pk=pk)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('todo_detail', pk=todo.pk)
	else:
		form = TodoForm(instance=todo)
	return render(request, 'todo/todo_edit.html', {'form': form})
# Create your views here.
