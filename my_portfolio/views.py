from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime

def my_portfolio(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.date = datetime.today().date()
            contact.save()
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I’ll get back to you as soon as possible.")
            return redirect('my_portfolio')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "index.html", {'form': form})
