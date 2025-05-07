# main/middleware.py

from django.shortcuts import redirect

class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.get_host() == 'mwexpert-1.onrender.com':
            return redirect(f'https://mwexpert.com{request.get_full_path()}')
        return self.get_response(request)
