from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import User_Male,User_Female,question_responses
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Login(request):
    if request.user.is_authenticated():
        user_details = User_Male.objects.filter(basic_details = request.user)
        if len(user_details) == 0:
            user_details = User_Female.objects.filter(basic_details = request.user)
            all_users = User_Male.objects.all()
        else:
            all_users = User_Female.objects.all()
        return render(request,"Login/main.html",{"user":request.user,"user_details":user_details[0],"all_users":all_users})
    else:
        return render(request,'Login/Login.html',{})

@csrf_exempt
def Verify(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        user = authenticate(username = username,password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                user_details = User_Male.objects.filter(basic_details = request.user)
                if len(user_details) == 0:
                    user_details = User_Female.objects.filter(basic_details = request.user)
                    all_users = User_Male.objects.all()
                else:
                    all_users = User_Female.objects.all()
                return render(request,"Login/main.html",{"user":user,"user_details":user_details[0],"all_users":all_users})
        else:
            return redirect("/")
    else:
        return redirect("/")

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        if (User.objects.filter(username = request.POST['uname'])).exists():
            return redirect("Login:Login")
        else:
            user = User.objects.create_user(username = request.POST['uname'],password=request.POST['password'],email = request.POST['email'])
            user.first_name = request.POST['fname']
            user.last_name = request.POST['lname']
            user.save()
            if (request.POST['gender'] == "male"):
                d = (request.POST['dob']).split("-")
                date = d[0]+"-"+d[1]+"-"+d[2]
                new_u = User_Male(basic_details = user,mobile_number = int(request.POST['m_no']),date_of_birth = date,profile_picture = request.FILES['profile_pic'])
                if (request.POST['premium'] == "yes"):
                    new_u.premium_user = True
                else:
                    new_u.premium_user = False
                new_u.save()
                return render(request,"Login/questions.html",{"user":user})
            else:
                d = (request.POST['dob']).split("-")
                date = d[0]+"-"+d[1]+"-"+d[2]
                new_u = User_Female(basic_details = user,mobile_number = int(request.POST['m_no']),date_of_birth = date,profile_picture = request.FILES['profile_pic'])
                if (request.POST['premium'] == "yes"):
                    new_u.premium_user = True
                else:
                    new_u.premium_user = False
                new_u.save()
                return render(request,"Login/questions.html",{"user":user})
    else:
        return redirect('/')

def Logout(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect("Login:Login")
    else:
        return redirect("Login:Login")

def user_details(request,username):
    if request.user.is_authenticated():
        use = User.objects.get(username = username)
        user_details = User_Male.objects.filter(basic_details = use)
        u = User_Male.objects.filter(basic_details = request.user)
        if len(user_details) == 0:
            user_details = User_Female.objects.filter(basic_details = use)
        if len(u) == 0:
            u = User_Female.objects.filter(basic_details = request.user)
        return render(request,'Login/user_details.html',{"user_det":user_details[0],"user":request.user,"user_details":u[0],"question_responses":question_responses.objects.get(basic_details = use)})
    else:
        return redirect("/")

@csrf_exempt
def user_det(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            username = request.POST["q"]
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return HttpResponse("<h1>"+"No Such User"+"<br>"+"Please Go back and Check the Spelling"+"</h1>")
            user_details = User_Male.objects.filter(basic_details = user)
            u = User_Male.objects.filter(basic_details = request.user)
            if len(user_details) == 0:
                user_details = User_Female.objects.filter(basic_details = request.user)
            if len(u) == 0:
                u = User_Female.objects.filter(basic_details = request.user)
            return render(request,'Login/user_details.html',{"user_det":user_details[0],"user":request.user,"user_details":u[0],"question_responses":question_responses.objects.get(basic_details = user)})
        else:
            return redirect("/")
    else:
        return redirect("/")

@csrf_exempt
def question_res(request):
    if request.method == "POST":
        username = request.POST['name']
        user = User.objects.get(username = username)
        response = question_responses(basic_details = user)
        response.question1 = request.POST['question1']
        response.question2 = request.POST['question2']
        response.question3 = request.POST['question3']
        response.question4 = request.POST['question4']
        response.question5 = request.POST['question5']
        response.save()
        return redirect("/")
    else:
        return redirect("/")

def Most_Compatible(request):
    if request.user.is_authenticated():
        user_details = User_Male.objects.filter(basic_details = request.user)
        if len(user_details) == 0:
            user_details = User_Female.objects.filter(basic_details = request.user)
            all_users = User_Male.objects.all()
        else:
            all_users = User_Female.objects.all()
        return render(request,"Login/Most_Compatible.html",{"user":request.user,"user_details":user_details[0],"all_users":all_users})
    else:
        return redirect("/")
