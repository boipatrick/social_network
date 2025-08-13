from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exists")
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "User created successfully")
                return render(request, 'signup.html')


                #login the user after signup
                #profile object
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                red          

        else:
            messages.info(request, "Passwords do not match")
            return render(request, 'signup.html')
        # Here you would typically handle user creation and validation
        # For example, check if passwords match, create a user, etc.

        # Redirect or render a success page after signup
    else:
        return render(request, 'signup.html')  # Redirect to index or another page
    

