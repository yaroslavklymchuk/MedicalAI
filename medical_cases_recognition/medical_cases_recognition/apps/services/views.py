from django.shortcuts import render


def ResponseForServices(request):
    return render(request, "services.html", locals())