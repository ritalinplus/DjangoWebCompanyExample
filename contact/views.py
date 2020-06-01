from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Sending email
            email_to_send = EmailMessage (
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["Caffettiera@mailtrap.com"], # This email es totally fake
                reply_to=[email]
            )

            try:
                email_to_send.send()
                return redirect(reverse('contact') + '?ok')

            except Exception:
                return redirect(reverse('contact') + '?fail')

    return render(request, "contact/contact.html", {"form": contact_form})
