from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def tutor_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()  # Save many-to-many relationships (like 'classes')
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

