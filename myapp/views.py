from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
# Create your views here.
def home_view(request):
    return render(request, 'index.html')
@csrf_exempt # Use this decorator for simplicity with external forms
def contact_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            # Basic validation
            if not all([name, email, message]):
                return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)

            # Prepare the email
            subject = f'New Contact Form Submission from {name}'
            message_body = f"""
            You have received a new message from your website contact form:

            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            sender_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER] # Sends the email to yourself

            # Send the email
            send_mail(subject, message_body, sender_email, recipient_list)

            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
