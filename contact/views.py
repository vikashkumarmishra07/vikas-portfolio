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

        # -------------------------------
        # 1️⃣ Email to YOU
        # -------------------------------
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
            settings.EMAIL_HOST_USER,
            ['vikas771734@gmail.com'],  # Your email
            fail_silently=False,
        )

        # -------------------------------
        # 2️⃣ Confirmation Email to USER
        # -------------------------------
        send_mail(
    "We Received Your Message",
    f"""
    Hi {name},

    Thank you for contacting me.

    Here is a copy of your message:

    Subject: {subject}
    Message: {message}

    I will reply to you soon.

    Regards,
    Vikash Kumar Mishra
    """,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)

        messages.success(request, "Message Sent Successfully!")
        return redirect('/#contact')

    return render(request, 'index.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def dashboard(request):
    messages_data = Contact.objects.all().order_by('-created_at')
    total_messages = messages_data.count()

    return render(request, "dashboard.html", {
        "messages": messages_data,
        "total_messages": total_messages
    })


@login_required
def mark_as_read(request, id):
    msg = get_object_or_404(Contact, id=id)
    msg.is_read = True
    msg.save()
    return redirect("dashboard")


@login_required
def delete_message(request, id):
    msg = get_object_or_404(Contact, id=id)
    msg.delete()
    return redirect("dashboard")