from django.shortcuts import render

def HomePageView(request):
    context = {}
    context['msg'] = 'The View is Functioning'
    return render(request, 'pages/home-page.html', context)