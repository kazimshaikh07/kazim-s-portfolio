from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from my_portfolio.models import Contact
import os
from django.contrib import messages
from django.conf import settings

# Create your views here.
def my_portfolio(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            # Skip DB write on Vercel if no DATABASE_URL set
            if (os.environ.get('VERCEL') or os.environ.get('VERCEL_URL')) and not os.environ.get('DATABASE_URL'):
                messages.success(request, "Thank you! Message received (demo mode).")
                return redirect('my_portfolio')
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                message=message_text,
                date=datetime.today().date(),
            )
            contact.save()
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I’ll get back to you as soon as possible.")
            return redirect('my_portfolio')  # Post/Redirect/Get to avoid resubmission
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, "index.html")