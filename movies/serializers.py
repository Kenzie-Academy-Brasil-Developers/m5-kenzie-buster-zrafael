from rest_framework import serializers
from .models import Movie, RatingChoice, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, required=False)
    rating = serializers.ChoiceField(choices=RatingChoice.choices, default=RatingChoice.G, allow_null=True)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(read_only=True)
    
    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj:MovieOrder):
        return obj.movie.title


    def get_buyed_by(self, obj:MovieOrder):
        return obj.buyer.email


    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)