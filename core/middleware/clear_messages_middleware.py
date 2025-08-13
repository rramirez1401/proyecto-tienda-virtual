from django.contrib import messages

class ClearStaleMessagesMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Consumir mensajes antes de la vista
        list(messages.get_messages(request))
        response = self.get_response(request)
        return response
