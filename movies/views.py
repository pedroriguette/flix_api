from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status
from app.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import MovieSeriliazer, MovieStatsSerializer, MovieListSerializer
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListSerializer
        return MovieSeriliazer


class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieSeriliazer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get(self, request):         # rescrevendo o endpoint get
        total_movies = self.queryset.count()
        movies_by_genres = self.queryset.values(
            'genres__name').annotate(count=Count('id'))         # total de movies cadastrado por genero
        total_reviews = Review.objects.count()          # total de reviews
        average_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']            # média de reviews

        data = {
            'total_movies': total_movies,
            'movies_by_genres': movies_by_genres,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1 if average_stars else 0),
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)           # mostra uma mensagem de erro
        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )             # devolver resposta
