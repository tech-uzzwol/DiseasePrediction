from profile import Profile
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import signUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from hospitalApp.models import contactEnquiry
from .models import Appointment
from django.utils import timezone
from .models import HeartDisease

# from sklearn.externals import joblib
import joblib
import numpy as np




# from .models import Patient
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def diabetes(request):
    return render(request,'diabetes.html',{})


def braintumor(request):
    return render(request,'braintumor.html',{})

def heartdisease(request):
    return render(request,'heartdisease.html',{})

def breastcancer(request):
    return render(request,'breastcancer.html',{})


def breastcancerPrediction(request):
    model = joblib.load('breastcancer_model.pkl')
    
    radius = int(request.POST.get('radius'))
    texture = int(request.POST.get('texture'))
    perimeter = int(request.POST.get('perimeter'))
    area = int(request.POST.get('area'))
    smoothness = int(request.POST.get('smoothness'))
    compactness = int(request.POST.get('compactness'))
    concavity = int(request.POST.get('concavity'))
    concavePoints = int(request.POST.get('concavePoints'))
    symmetry = int(request.POST.get('symmetry'))
    fractalDimemsion = int(request.POST.get('fractalDimemsion'))
    
    radiusse = int(request.POST.get('radiusse'))
    texturese = int(request.POST.get('texturese'))
    perimeterse = int(request.POST.get('perimeterse'))
    arease = int(request.POST.get('arease'))
    smoothnessse = int(request.POST.get('smoothnessse'))
    compactnessse = int(request.POST.get('compactnessse'))
    concavityse = int(request.POST.get('concavityse'))
    concavePointsse = int(request.POST.get('concavePointsse'))
    symmetryse = int(request.POST.get('symmetryse'))
    fractalDimemsionse = int(request.POST.get('fractalDimemsionse'))
    
    radiusWorst = int(request.POST.get('radiusWorst'))
    textureWorst = int(request.POST.get('textureWorst'))
    perimeterWorst = int(request.POST.get('perimeterWorst'))
    areaWorst = int(request.POST.get('areaWorst'))
    smoothnessWorst = int(request.POST.get('smoothnessWorst'))
    compactnessWorst = int(request.POST.get('compactnessWorst'))
    concavityWorst = int(request.POST.get('concavityWorst'))
    concavePointsWorst = int(request.POST.get('concavePointsWorst'))
    symmetryWorst = int(request.POST.get('symmetryWorst'))
    fractalDimemsionWorst = int(request.POST.get('fractalDimemsionWorst'))
    
    
    X = np.array([[radius, texture, perimeter, area, smoothness, compactness, concavity, concavePoints, symmetry, fractalDimemsion,
                   radiusse, texturese, perimeterse, arease, smoothnessse, compactnessse, concavityse, concavePointsse, symmetryse, fractalDimemsionse, 
                   radiusWorst, textureWorst, perimeterWorst, areaWorst, smoothnessWorst, compactnessWorst, concavityWorst, concavePointsWorst, symmetryWorst, fractalDimemsionWorst]])
    print(X)
    prediction = model.predict(X)
    
    if prediction[0] == 0:
        result = 'Your cancer is Benign'
    else:
        result = 'Your Cancer is Melignant'
        
    return render(request, 'breasecancerresult.html', {'result': result})



def heartdiseasePrediction(request):
    model = joblib.load('heartdisease.pkl')
    age = int(request.POST.get('age'))
    sex = int(request.POST.get('sex'))
    chestPain = int(request.POST.get('chestPain'))
    restingBloodPressure = int(request.POST.get('restingBloodPressure'))
    cholesterol = int(request.POST.get('cholesterol'))
    fastingBloodSugar = int(request.POST.get('fastingBloodSugar'))
    restingElectrocardiographic = int(request.POST.get('restingElectrocardiographic'))
    maximumHeartRate = int(request.POST.get('maximumHeartRate'))
    ExerciseInducedAngina = int(request.POST.get('ExerciseInducedAngina'))
    STdepression = float(request.POST.get('STdepression'))
    slope = int(request.POST.get('slope'))
    ca = int(request.POST.get('ca'))
    thal = int(request.POST.get('thal'))
   
    X = np.array([[age, sex, chestPain, restingBloodPressure, cholesterol, fastingBloodSugar, restingElectrocardiographic, maximumHeartRate, ExerciseInducedAngina, STdepression, slope, ca, thal]])
    print(X)
    prediction = model.predict(X)
    
    if prediction[0] == 0:
        result = 'Your heart is healthy'
    else:
        result = 'Your heart is unhealthy'
        
    return render(request, 'heartdiseaseresult.html', {'result': result})





def diabetesprediction(request):
    model = joblib.load('diabetes_model.pkl')
    pregnancies = int(request.POST.get('pregnancies'))
    glucose = int(request.POST.get('glucose'))
    bp = int(request.POST.get('bp'))
    st = int(request.POST.get('st'))
    insulin = int(request.POST.get('insulin'))
    bmi = int(request.POST.get('bmi'))
    dp = int(request.POST.get('dp'))
    age = int(request.POST.get('age'))
    
    X = np.array([[pregnancies, glucose, bp, st, insulin, bmi, dp, age]])
    print(X)
    prediction = model.predict(X)
    
    if prediction[0] == 0:
        result = 'Congratulations! You dont have Diabetes'
    else:
        result = 'Sorry!! you have Diabetes'
    return render(request, 'diabetesresult.html', {'result': result})





def breastcancer(request):
    return render(request,'breastcancer.html',{})

def appointment(request):
    return render(request,'appointment.html',{})

# this is for contact us form
def saveEnquiry(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        emaill = request.POST.get('email')
        subjectt = request.POST.get('subject')
        messagess = request.POST.get('message')
        # here left side is the model field name .........
        en=contactEnquiry(your_name = name, your_email = emaill, subject = subjectt, messages = messagess)
        en.save()
    return render(request,"contact.html")

def save_appointment(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        specialty = request.POST.get('specialty')
        date = timezone.datetime.strptime(request.POST['date'], '%m/%d/%Y').strftime('%Y-%m-%d')
        time = timezone.datetime.strptime(request.POST['time'], '%I:%M%p').time()
        msg = request.POST.get('message')


        if name and name.strip() != "" :
            en = Appointment(name=name, email=email, contact=contact, date=date, time=time, messages=msg, specialty=specialty)
            en.save()
            messages.success(request, 'Appointment saved successfully')
            # return HttpResponse("Appointment saved successfully.")
        else:
            messages.error(request, 'Error: Name is required')
            return redirect('appointment')
            # return HttpResponse("Error: Name is required.")   

    return render(request, 'appointment.html')

def signin(request):

    # if request.method =='POST':
    #      Email= request.POST['Email']
    #      Password= request.POST['password']

    #      user =auth.authenticate(Email='Email' , Password='password')

    #      if user is not None:
    #         auth.login(request,user)
    #         return render('home')
    #      else:
    #         messages.info(request, 'Credentials Invalid')
    #         return render('signin')
    # else:
    

     return render(request,'signin.html',{})

def signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = signUpForm()
    return render (request=request, template_name="signup.html", context={"signUpForm":form})

def contact(request):
    return render(request,'contact.html',{})


def services(request):
    return render(request,'services.html',{})

def doctors(request):
    return render(request,'doctors.html',{})


def about(request):
    return render(request,'about.html',{})


     