from rest_framework.views import APIView, Request, Response, status
from .serializers import RegisterSerializer
from .models import Account
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwnerOrIsEmployee

class UserView(APIView):
    def get(self, request:Request) -> Response:
        users = Account.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request:Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrIsEmployee]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(Account, id=user_id)
        self.check_object_permissions(request, user)
        serializer = RegisterSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(Account, id=user_id)
        self.check_object_permissions(request, user)
        serializer = RegisterSerializer(user, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_200_OK)
