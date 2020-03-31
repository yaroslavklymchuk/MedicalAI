from django.shortcuts import render
from .forms import GeneralForm, UserForm
from django.http import HttpResponse


def ResponseForSubscribe(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        general_form = GeneralForm(request.POST, request.FILES)

        if general_form.is_valid() and user_form.is_valid():
            user_form.save()
            general_form.save()

            return render(request, "subscribe_result.html")
        else:
            return HttpResponse('subscribe failed with errors: {}'.format(user_form.errors))
    else:
        raw_user_form = UserForm()
        raw_general_form = GeneralForm()
        return render(request, "subscribe.html",
                      {'user_form': raw_user_form,
                       'general_form': raw_general_form
                       })

