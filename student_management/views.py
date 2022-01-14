from django.shortcuts import render,redirect
from .models import StudentInfo,StudentAcademics
from .forms import UserRegisterForm,StudentinfoForm
from django.contrib.auth.models import User,auth
from .serializers import StudentInfoSerializer,StudentAcademicsSerializer

context = {
        "student":{},
        "logs":False,
    }

# Home view
def home(request):

    # creating object for all ssudents information
    student_data=StudentInfo.objects.all()

    # passing data of students to dictionary
    context["student"]=student_data

    # rendering home.html with students data
    return render(request,'home.html',context)

# signup view
def signup(request):

    # checking for request method
    if request.method == 'POST':
        # creating form for user signup
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # saving form
            form.save()

            # redirecting to home.html
            return redirect('home')

    # if there is error in sign up of user then it will again render signup.html
    return render(request, 'signup.html', {'form': form})

# login view
def login(request):

    if request.method=="POST":
        # getting username and password from user
        username=request.POST['username']
        password=request.POST['password']

        # authenticating for login
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)

            # setting logs key as true as user successfully logged in
            context["logs"]=True

            # redirecting to home.html
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        # if there is error in login of user then it will again render login.html
        return render(request,'login.html')

# logout view
def logout(request):
    # after logout event setting logs as false
    context["logs"]=False

    # redirecting to home 
    return redirect('home')

# search view
def search(request):

    if request.method == 'POST':
        # getting data from user and converting it to dictionary
        data=request.POST.dict()

        # converting request data to camel case for searching of specific student
        temp=data['search']
        temp=temp.title()
        data['search']=temp

        student_data=StudentInfo.objects.all()
        context["student"]=student_data

        # searching for student
        student=StudentInfo.objects.filter(Name=data['search'])

        if student:
            # creating serializer object for searched student 
            serializer=StudentInfoSerializer(student,many=True)
            context["student"]=serializer.data

        else:
            print("not found")
    # rendering home.html
    return render(request,'home.html',context)

# addstudent view
def addstudent(request):

    if request.method == 'POST':
        # creating student information form
        form = StudentinfoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:

        form = StudentinfoForm()
    # rendering addstudentform.html for adding student
    return render(request,'addstudentform.html', {'form': form})

# delete view 
def delete(request):

    if request.method=='GET':

        data=request.GET.dict()

        student=StudentInfo.objects.filter(Name=data['d'])
        # deleting record of student
        student.delete()

    return redirect('home')







