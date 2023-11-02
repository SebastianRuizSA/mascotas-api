from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Raza, Perro
from .serializers import RazaSerializer, PerroSerializer
import json

class RazaList(View):
    def get(self, request):
        razas = Raza.objects.all()
        serializer = RazaSerializer(razas, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = RazaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class RazaDetail(View):
    def get(self, request, raza_id):
        raza = get_object_or_404(Raza, pk=raza_id)
        serializer = RazaSerializer(raza)
        return JsonResponse(serializer.data)

    def put(self, request, raza_id):
        raza = get_object_or_404(Raza, pk=raza_id)
        data = json.loads(request.body)
        serializer = RazaSerializer(raza, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, raza_id):
        raza = get_object_or_404(Raza, pk=raza_id)
        raza.delete()
        return JsonResponse({'message': 'Raza borrada con exito'}, status=204)

class PerroList(View):
    def get(self, request):
        perros = Perro.objects.all()
        serializer = PerroSerializer(perros, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = PerroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class PerroDetail(View):
    def get(self, request, perro_id):
        perro = get_object_or_404(Perro, pk=perro_id)
        serializer = PerroSerializer(perro)
        return JsonResponse(serializer.data)

    def put(self, request, perro_id):
        perro = get_object_or_404(Raza, pk=perro_id)
        data = json.loads(request.body)
        serializer = PerroSerializer(perro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, perro_id):
        perro = get_object_or_404(Raza, pk=perro_id)
        perro.delete()
        return JsonResponse({'message': 'Perro borrado con exito'}, status=204)