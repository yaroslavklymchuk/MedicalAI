from django.shortcuts import render


def ResponseForDetection(request):
    return render(request, "detect.html", locals())