from django.shortcuts import render


def profile(request):
    """ User profile """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)