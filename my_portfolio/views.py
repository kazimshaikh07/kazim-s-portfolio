from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

def my_portfolio(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.date = datetime.today().date()
            contact.save()

            # Prepare and send email
            subject = f"New Contact Form Submission from {form.cleaned_data['name']}"
            message = f"""
            You have received a new message from your portfolio contact form:

            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            
            Message:
            {form.cleaned_data['message']}
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I’ll get back to you as soon as possible.")
            except Exception as e:
                # For debugging purposes, you might want to print the error
                print(f"Email sending error: {e}")
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")

            return redirect('my_portfolio')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "index.html", {'form': form})
