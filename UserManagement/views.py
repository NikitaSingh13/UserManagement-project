from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h1>Welcome to UserManagement Project</h1>"
        "<p>This is a test API built using Django REST Framework.</p>"
    )
