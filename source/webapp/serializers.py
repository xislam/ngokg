from abc import ABC

from rest_framework import serializers

from webapp.models import RankLibrary, RankLegislation, Legislation, QA


class RankLibrarySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    created_date = serializers.DateTimeField()
    edited_date = serializers.DateTimeField()
    deleted_date = serializers.DateTimeField()

    class Meta:
        model = RankLibrary
        fields = ['id', 'name', 'created_date', 'edited_date', 'deleted_date']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return RankLibrary.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class LibraryFromNGOSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rank = serializers.SlugRelatedField(queryset=RankLibrary.objects.all(), slug_field='name')
    name = serializers.CharField(max_length=250)
    description = serializers.CharField(style={'base_template'})
    files = serializers.FileField()
    created_date = serializers.DateTimeField()
    edited_date = serializers.DateTimeField()
    deleted_date = serializers.DateTimeField()

    class Meta:
        model = RankLibrary
        fields = ['id', 'rank', 'name', 'description', 'files', 'created_date', 'edited_date', 'deleted_date']


class RankLegislationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    created_date = serializers.DateTimeField()
    edited_date = serializers.DateTimeField()
    deleted_date = serializers.DateTimeField()

    class Meta:
        model = RankLegislation
        fields = ['id', 'name', 'created_date', 'edited_date', 'deleted_date']


class LegislationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rank = serializers.SlugRelatedField(queryset=RankLegislation.objects.all(), slug_field='name')
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(style={'base_template'})
    files = serializers.FileField()
    created_date = serializers.DateTimeField()
    edited_date = serializers.DateTimeField()
    deleted_date = serializers.DateTimeField()

    class Meta:
        model = Legislation
        fields = ['id', 'rank', 'name', 'description', 'files', 'created_date', 'edited_date', 'deleted_date']


class QASerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=1000)
    description = serializers.CharField(style={'base_template'})
    created_date = serializers.DateTimeField()
    edited_date = serializers.DateTimeField()
    deleted_date = serializers.DateTimeField()

    class Meta:
        model = QA
        fields = ['id', 'name', 'description', 'created_date', 'edited_date', 'deleted_date']
