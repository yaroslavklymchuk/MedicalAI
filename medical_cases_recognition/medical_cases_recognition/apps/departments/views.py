from django.shortcuts import render


def ResponseForDepartments(request):
    return render(request, "departments.html", locals())