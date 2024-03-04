from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # Implement your authentication logic here
            # Check if the username and password are valid
            # For example, query the User model and verify credentials
            try:
                user = User.objects.get(username=username, password=password)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)