from rest_framework import serializers
from .models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return None


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']
