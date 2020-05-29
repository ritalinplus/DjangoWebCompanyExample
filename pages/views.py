from django.shortcuts import render, get_object_or_404
from pages.models import Page


def page(request, page_id):
    page_obj = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page': page_obj})
