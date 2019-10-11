from rest_framework import serializers
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    body = serializers.CharField()
