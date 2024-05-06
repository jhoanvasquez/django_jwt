from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class HelloWorldView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        user = get_user_from_request(request)
        content = {'message': f'Hello, World! {user}'}
        return Response(content)

    def post(self, request):
        user = get_user_from_request(request)
        content = {'message': f"No authentication required with post! {user}"}
        return Response(content)

class NoAuthView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'No authentication required!'}
        return Response(content)

    def post(self, request):
        content = {'message': f'No authentication required with post!'}
        return Response(content)

def get_user_from_request(request):
    user, token = JWTAuthentication().authenticate(request)
    return user