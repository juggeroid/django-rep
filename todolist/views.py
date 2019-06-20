from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	todos = TodoList.objects.filter(author=request.user)
	categories = Category.objects.all()
	
	if request.method == "POST":
		if "taskAdd" in request.POST:
			author = request.user
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category"]
			content = title + " -- " + date + " " + category
			Todo = TodoList(author=author,
							title=title,
							content=content,
							due_date=date,
							category=Category.objects.get(name=category))
			Todo.save()
		
		if "taskDelete" in request.POST:
			try:
				checked_list = request.POST.getlist("checkedbox")
				for todo_id in checked_list:
					todo = TodoList.objects.get(id=int(todo_id))
					todo.delete()
			except:
				pass
				
		if "deleteAll" in request.POST:
			todos.delete()

	return render(request, "index.html", {"todos": todos, "categories": categories})
