from django.shortcuts import render


def view(request):
    return render(request=request,
                  template_name='home.html',
                  context={})




