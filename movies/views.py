from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from users.permissions import IsAdminOrReadOnly
from .models import Movie
from .permissions import TokenPermission
from .serializers import MovieSerializer, MovieOrderSerializer

# Create your views here.
class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request:Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request:Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request:Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request:Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TokenPermission]

    def post(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, buyer=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

