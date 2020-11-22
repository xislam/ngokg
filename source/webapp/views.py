from datetime import datetime
from itertools import chain

import requests
from django.core.serializers import serialize, deserialize
from django.db.models import Q
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from webapp.models import LibraryFromNGO, Question, Review, News
from webapp.serializers import *


@csrf_exempt
def rank_library_list(request):
    """
    List all code RankLibrary, or create a new RankLibrary.
    """
    if request.method == 'GET':
        rank_library = RankLibrary.objects.all()
        serializer = RankLibrarySerializer(rank_library, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RankLibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def rank_library_detail(request, pk):
    """
    Retrieve, update or delete a code RankLibrary.
    """
    try:
        rank_library = RankLibrary.objects.get(pk=pk)
    except RankLibrary.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RankLibrarySerializer(rank_library)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RankLibrarySerializer(rank_library, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rank_library.delete()
        return HttpResponse(status=204)



@csrf_exempt
def library_from_nko_list(request):
    """
    List all code LibraryFromNGO, or create a new LibraryFromNGO.
    """
    if request.method == 'GET':
        library_from_ngo = LibraryFromNGO.objects.all()
        serializer = LibraryFromNGOSerializer(library_from_ngo, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibraryFromNGOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def library_from_nko_detail(request, pk):
    """
    Retrieve, update or delete a code LibraryFromNGO.
    """
    try:
        library_from_ngo = LibraryFromNGO.objects.get(pk=pk)
    except LibraryFromNGO.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LibraryFromNGOSerializer(library_from_ngo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LibraryFromNGOSerializer(library_from_ngo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        library_from_ngo.delete()
        return HttpResponse(status=204)


@csrf_exempt
def rank_legislation_list(request):
    """
    List all code  RankLegislation, or create a new  RankLegislation.
    """
    if request.method == 'GET':
        rank_legislation = RankLegislation.objects.all()
        serializer = RankLegislationSerializer(rank_legislation, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RankLegislationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def rank_legislation_detail(request, pk):
    """
    Retrieve, update or delete a code  RankLegislation.
    """
    try:
        rank_legislation = RankLegislation.objects.get(pk=pk)
    except RankLegislation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RankLegislationSerializer(rank_legislation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RankLegislationSerializer(rank_legislation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rank_legislation.delete()
        return HttpResponse(status=204)


@csrf_exempt
def legislation_list(request):
    """
    List all code  Legislation, or create a new  Legislation.
    """
    if request.method == 'GET':
        legislation = Legislation.objects.all()
        serializer = LegislationSerializer(legislation, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LegislationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def legislation_detail(request, pk):
    """
    Legislation, update or delete a code  Legislation.
    """
    try:
        legislation = Legislation.objects.get(pk=pk)
    except Legislation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LegislationSerializer(legislation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LegislationSerializer(legislation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        legislation.delete()
        return HttpResponse(status=204)


@csrf_exempt
def qa_list(request):
    """
    List all code  QA, or create a new  QA.
    """
    if request.method == 'GET':
        qa = QA.objects.all()
        serializer = QASerializer(qa, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QASerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def qa_detail(request, pk):
    """
    QA, update or delete a code  QA.
    """
    try:
        qa = QA.objects.get(pk=pk)
    except QA.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QASerializer(qa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QASerializer(qa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        qa.delete()
        return HttpResponse(status=204)


class QuestionView(APIView):
    def post(self, request, *args, **kwargs):
        question = Question(
            name=request.data['name'],
            mail=request.data['mail'],
            text=request.data['text'],
        )
        question.save()
        return Response({"status": "success"})


class ReviewView(APIView):
    def post(self, request, *args, **kwargs):
        review = Review(
            stars=request.data['stars'],
            text=request.data['text'],
        )
        review.save()
        return Response({"status": "success"})


class SearchView(APIView):
    def post(self, request, *args, **kwargs):
        search_string = request.data['search']
        a = RankLibrary.objects.filter(Q(name__icontains=search_string))
        b = LibraryFromNGO.objects.filter(Q(name__icontains=search_string) | Q(description__icontains=search_string))
        c = RankLegislation.objects.filter(Q(name__icontains=search_string))
        d = Legislation.objects.filter(Q(name__icontains=search_string) | Q(description__icontains=search_string))
        e = QA.objects.filter(Q(name__icontains=search_string) | Q(description__icontains=search_string))
        for item in b:
            item.files = 'http://localhost:8000' + item.files.url
        for item in d:
            item.files = 'http://localhost:8000' + item.files.url
        result_list = list(chain(a, b, c, d, e))
        result_list = serialize('json', result_list)
        for obj in b:
            print(obj.files)
        return Response({"result": result_list})




