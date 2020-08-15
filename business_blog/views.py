from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Home Page
def home(request):
    context = {

    }

    return render(request, 'business_blog/index.html', context)

# About Page
def about(request):
    context = {

    }

    return render(request, 'business_blog/about.html', context)


# Contact Page
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['message']

        message = f'Moi\'s Business Blog: Contact Form...\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {text}\n\n'

        # Set up to send an email...
        send_mail(
            subject,  # Subject
            message,  # Message
            email,  # From email
            ['moimyazz@gmail.com'],  # To email
        )

        context = {
            'name': name,
        }
        render(request, 'business_blog/contact.html', context)
    else:
        context = {

        }

    return render(request, 'business_blog/contact.html', context)


# Services Page
def services(request):
    context = {

    }

    return render(request, 'business_blog/services.html', context)


# Projects Page
def project(request):
    context = {

    }

    return render(request, 'business_blog/project.html', context)


# Blog Home Page
def blog(request):
    context = {

    }

    return render(request, 'business_blog/blog.html', context)


# Blog Post Detail Page
def blog_details(request):
    context = {

    }

    return render(request, 'business_blog/blog_details.html', context)


# Elements Page
def elements(request):
    context = {

    }

    return render(request, 'business_blog/elements.html', context)
