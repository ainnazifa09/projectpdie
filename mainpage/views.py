#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from mainpage.models import Registration
from django.contrib import messages

def mainpage(request):
    return render(request, 'mainpage.html')

def studentregistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('idd')
        course = request.POST.get('course')
        phone_number = request.POST.get('numphone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Save the data to the database
        data = Registration(
            name=name,
            idd=student_id,
            course=course,
            numphone=phone_number,
            email=email,
            password=password
        )
        data.save()

        # Redirect to the sign-in page after successful registration
        return redirect('studentsignin')
    else:
        return render(request, 'studentregistration.html')

def profilepage(request):
    displaydata = Registration.objects.all().values()
    dict = {
        'displaydata': displaydata
    }
    return render(request, 'profilepage.html', dict)

def studentsignin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect('studentdashboard')  # Redirect to student dashboard upon successful login
        else:
            # Authentication failed
            error_message = "Invalid email or password. Please try again."
            return render(request, 'studentdashboard.html', {'error_message': error_message})
    
    # If request method is not POST (GET request or invalid form submission), render the signin form
    return render(request, 'studentsignin.html')

def lecturersignin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('lecturerdashboard')
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 'lecturerdashboard.html', {'error_message': error_message})
    
    return render(request, 'lecturersignin.html')

def lecturerdashboard(request):
    return render(request, 'lecturerdashboard.html')

def studentdashboard(request):
    return render(request, 'studentdashboard.html')

