from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializers
from actors.serializers import ActorsSerializers


class MovieSeriliazer(serializers.ModelSerializer):
    # campo calculavel
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    # objetos que serão calculados
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)

        return None

    def validate_realease_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'Filmes Anteriores a 1970 não é possivel cadastrar'
            )
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'Não é possivel escrever mais de 300 caracteres'
            )
        return value


class MovieListSerializer(serializers.ModelSerializer):
    actors = ActorsSerializers(many=True)
    genres = GenreSerializers()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genres', 'actors', 'release_date', 'rate', 'resume']

    # objetos que serão calculados
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genres = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
