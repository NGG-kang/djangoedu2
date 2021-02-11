from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            send_mail('Subject here', 'Here is the message.', 'skarndrkd1222@gmail.com', ['skarndrkd1222@gmail.com'],
                      fail_silently=False)
            user = form.save()
            messages.success(request, "회원가입 환영합니다")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form
    })