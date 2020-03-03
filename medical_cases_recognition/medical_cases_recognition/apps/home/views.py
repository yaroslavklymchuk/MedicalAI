from django.shortcuts import render


def ResponseForHome(request):
    return render(request, "index.html", locals())