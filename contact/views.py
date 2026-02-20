from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send Email
        full_message = f"""
        New message from Portfolio Website

        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  # from
            ['vikas771734@gmail.com'], # to (your email)
            fail_silently=False,
        )

        messages.success(request, "Message Sent Successfully!")
        return redirect('/#contact')

    return render(request, 'index.html')
