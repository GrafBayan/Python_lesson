from django.shortcuts import render
from django.views.generic import TemplateView


def def_func_template(request):
    return render(request, 'second_task/class_template.html')

class Class_template(TemplateView):
    def get(self, request):
        return render(request, 'second_task/func_template.html')