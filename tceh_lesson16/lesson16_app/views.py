from django.shortcuts import render
from lesson16_app.forms import BlogPostForm
from lesson16_app.models import Storage, BlogPostModel
from django.contrib import messages

# Create your views here.


def index(request):
    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            model = BlogPostModel(form.data)
            all_items.append(model)
            messages.success(request, 'Posted!')
        else:
            messages.error(request, 'Validation failed')
        return render(request, 'my_templates/index.html', {
            'form': form, 'items': all_items
        })
    else:
        form = BlogPostForm()
        return render(request, 'my_templates/index.html', {
            'form': form, 'items': all_items
        })
