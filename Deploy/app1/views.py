from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm, UserImageForm
from django.contrib import messages
from . models import UserImageModel
import joblib
import numpy as np
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserImageModel
from .forms import UserImageForm
import numpy as np
import joblib
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import UserImageForm
from sklearn.metrics import precision_recall_curve
from django.shortcuts import render
from django.core.mail import EmailMessage

from django.shortcuts import render
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import numpy as np
import joblib
from . import forms
from .models import UserImageModel

import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False
import time
from  joblib import load
import serial


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, '2_register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_login.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')

@ login_required
def index(request):
    return render(request, '4_home.html')


def landingpage(request):
    return render(request, '1_landingpage.html')

@ login_required
def problem_statement(request):
    return render(request, '5_problem_statement.html')



@ login_required
def model(request):
    print("HI")
    if request.method == "POST":
        form = forms.UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance
        #('obj',obj)

        result1 = UserImageModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/AASHIK/Music/FRUITS IMAGE & LEAF DETECTION(DONE)/FRUITS IMAGE & LEAF DETECTION(DONE)/Deploy/app1/FRUIT LEAVES.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/AASHIK/Music/FRUITS IMAGE & LEAF DETECTION(DONE)/FRUITS IMAGE & LEAF DETECTION(DONE)/Deploy/media/images/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Apple_Affected','Apple_healthy','Grape_Affected','Grape_healthy','Potato_Affected','Potato_healthy','Strawberry_Affected','Strawberry_healthy','Tomato_Affected','Tomato_healthy']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'Apple_Affected':
            a = 'FOUND THIS IMAGE IS Apple Affected'
        elif a == 'Apple_healthy':
            a = 'FOUND THIS IMAGE IS Apple healthy'
        elif a == 'Grape_Affected':
            a = 'FOUND THIS IMAGE IS Grape Affected'
        elif a == 'Grape_healthy':
            a = 'FOUND THIS IMAGE IS Grape healthy'
        elif a == 'Potato_Affected':
            a = 'FOUND THIS IMAGE IS Potato Affected'
        elif a == 'Potato_healthy':
            a = 'FOUND THIS IMAGE IS Potato healthy'
        elif a == 'Strawberry_Affected':
            a = 'FOUND THIS IMAGE IS Strawberry Affected'
        elif a == 'Strawberry_healthy':
            a = 'FOUND THIS IMAGE IS Strawberry healthy'
        elif a == 'Tomato_Affected':
            a = 'FOUND THIS IMAGE IS Tomato Affected'
        elif a == 'Tomato_healthy':
            a = 'FOUND THIS IMAGE IS Tomato healthy'
        else:
            a = 'WRONG INPUT'

        data = UserImageModel.objects.latest('id')
        data.label = a
        data.save()
        
        return render(request, 'output.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = forms.UserImageForm()
    return render(request, 'model.html',{'form':form})


@ login_required
def model1(request):
    print("HI")
    if request.method == "POST":
        form = forms.UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance
        #('obj',obj)

        result1 = UserImageModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/AASHIK/Music/FRUITS IMAGE & LEAF DETECTION(DONE)/FRUITS IMAGE & LEAF DETECTION(DONE)/Deploy/app1/FRUITS.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/AASHIK/Music/FRUITS IMAGE & LEAF DETECTION(DONE)/FRUITS IMAGE & LEAF DETECTION(DONE)/Deploy/media/images/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['freshapples','freshbanana','freshoranges','rottenapples','rottenbanana','rottenoranges']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        ser = serial.Serial("COM3", 9600)

        if a == 'freshapples':
            
            ser.write(b'A')
            ser.close()
            b = 'FOUND THIS IMAGE IS Freshapples'
        elif a == 'freshbanana':
            ser.write(b'C')
            ser.close()
            b = 'FOUND THIS IMAGE IS Freshbanana'
        elif a == 'freshoranges':
            ser.write(b'E')
            ser.close()
            b = 'FOUND THIS IMAGE IS Freshoranges'
        elif a == 'rottenapples':
            
            ser.write(b'B')
            ser.close()
            b = 'FOUND THIS IMAGE IS Rottenapples'
        elif a == 'rottenbanana':
           
            ser.write(b'D')
            ser.close()
            b = 'FOUND THIS IMAGE IS Rottenbanana'
        elif a == 'rottenoranges':
            ser.write(b'F')
            ser.close()
            b = 'FOUND THIS IMAGE IS Rottenoranges'
        else:
            b = 'WRONG INPUT'

        data = UserImageModel.objects.latest('id')
        data.label = a
        data.save()
        
        return render(request, 'output1.html',{'form':form,'obj':obj,'predict':b})
    else:
        form = forms.UserImageForm()
    return render(request, 'model1.html',{'form':form})

    
@ login_required
def model_database(request):
    models = UserImageModel.objects.all()
    return render(request, 'model_database.html', {'models':models})
    

