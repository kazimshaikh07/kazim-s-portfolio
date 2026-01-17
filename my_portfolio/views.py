from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def my_portfolio(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Save to Database
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
                
                # Check if email credentials are configured
                if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
                    logger.warning("Email credentials not configured. Contact form saved but email not sent.")
                    messages.success(request, "Thank you for reaching out! Your message has been saved.")
                else:
                    try:
                        send_mail(
                            subject,
                            message,
                            settings.DEFAULT_FROM_EMAIL,
                            [settings.ADMIN_EMAIL],
                            fail_silently=True,  # Don't block the request waiting for email
                        )
                        messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I'll get back to you as soon as possible.")
                    except Exception as email_error:
                        # Log email error but don't fail the form submission
                        logger.error(f"Failed to send email: {str(email_error)}", exc_info=True)
                        messages.success(request, "Thank you for reaching out! Your message has been saved. I'll get back to you soon.")
            except Exception as e:
                # Log the specific error for debugging
                logger.error(f"Error processing contact form: {str(e)}", exc_info=True)
                print(f"Error processing contact form: {e}")
                messages.error(request, f"Sorry, there was an error sending your message. Please try again later.")

            return redirect('my_portfolio')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "index.html", {'form': form})
