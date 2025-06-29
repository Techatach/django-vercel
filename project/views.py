from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def department(request):
    return render(request, 'department.html')

def department_single(request):
    return render(request, 'department_single.html')

def doctor(request):
    return render(request, 'doctor.html')

def doctor_single(request):
    return render(request, 'doctor-single.html')

def appointment(request):
    return render(request, 'appointment.html')

def blog_sidebar(request):
    return render(request, 'blog_sidebar.html')

def blog_single(request):
    return render(request, 'blog_single.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def ai(request):
    return render(request, 'ai.html')

def heart_form(request):
    return render(request, 'heart-form.html')

def heart_result(request):
    return render(request, 'heart-result.html')

