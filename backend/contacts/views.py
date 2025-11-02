from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Contact

def index(request):
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST"])
def submit_contact(request):
    try:
        data = json.loads(request.body)
        
        contact = Contact.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message')
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'There was an error submitting your message. Please try again.'
        }, status=400)