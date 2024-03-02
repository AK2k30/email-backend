from django.shortcuts import render, redirect
from .forms import UserSubmissionForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home_view(request):
    message = ''
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Your information has been submitted successfully!'
            # form = UserSubmissionForm() 
            return redirect('https://giveway.mygiveway.tech/thankyou')# Reset form
    else:
        form = UserSubmissionForm()
    return render(request, 'index.html', {'form': form, 'message': message})
