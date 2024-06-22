from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User, Task

# def all_tasks_detail(request):
#     data = Task.objects.all()
#     return JsonResponse(list(data.values()), safe=False)

# def task_detail(request, task_id):
#     task = Task.objects.get(id=task_id)
#     data = {
#         'id': task.id,
#         'title': task.title,
#         'description': task.description,
#         'status': task.status,
#         'priority': task.priority,
#         'due_date': task.due_date,
#         'category': task.category,
#         'assigned_to': task.assigned_to
#     }
    # return JsonResponse(data)
    # return render(request, 'task.html', {'form': form})

# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#         else:
#             form.save()
#         return redirect('task_list')

# def task_update(request, id):
#     task = 

# def task_delete(request, id):
#     task = get_object_or_404(Task, )

def index(request):
    in_progress_tasks = Task.objects.filter(status='in_progress')
    completed_tasks = Task.objects.filter(status='completed')
    overdue_tasks = Task.objects.filter(status='overdue')
    context = {
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
    }
    return render(request, 'index.html', context)

def search_view(request):
    if request.method == "POST":
        query = request.POST.get("query")
        results = Task.objects.filter(name__icontains=query)
        return JsonResponse(list(results.values()), safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def update_task_status(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        new_status = request.POST.get('status')
        if new_status in ['in-progress', 'completed', 'overdue']:
            task.status = new_status
            task.save()
            return JsonResponse({'status': 'success', 'task': task.id})
    return JsonResponse({'status': 'error'}, status=400)