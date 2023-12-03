from django.utils import timezone
from datetime import datetime
from events.models import UserVisit

class UpdateLastVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UserVisit.objects.update_or_create(
                user=request.user,
                defaults={'last_visit': timezone.now()}
            )
            
        response = self.get_response(request)
        return response