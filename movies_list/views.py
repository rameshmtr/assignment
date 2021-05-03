from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .models import Collections
from .serializers import CollectionsSerializers
from rest_framework.permissions import IsAuthenticated
import requests, json


class MoviesView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        movies_api = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0','Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
        movies_api.text
        movies_api.headers['content-type']
        result = movies_api.json()

        return Response(result)


class CollectionsView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        queryset = Collections.objects.all()

        if kwargs.get('pk'):
            instance = queryset.get(id=kwargs.get('pk'))
            return Response(CollectionsSerializers(instance).data)

        else:
            genres = []
            for instance in queryset:
                for result_instance in  list(eval(instance.movies)):
                    genres.extend(result_instance.get('genres').split(','))
            
            total_count={}
            for genre in genres:
                genre_count = genres.count(genre)
                total_count[genre] = genre_count
            
            three_genres = sorted(total_count, key=total_count.get, reverse=True)[:3]

            response = {}
            data = {}
            collection_response = [] 
            for instance in queryset:
                collection_response.append({'title':instance.title,
                                            'description':instance.description,
                                            'uuid':instance.id})

            data['collections'] = collection_response
            data['favourite_genres'] = ','.join([str(elem) for elem in three_genres])
            response['is_success'] = True
            response['data'] = data

            return Response(response)

    def post(self, request):

        queryset = Collections.objects.all()
        serializer_class = CollectionsSerializers

        movies_api = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0','Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
        movies_api.text
        movies_api.headers['content-type']
        result = movies_api.json()

        movies_list = []
        for results in result.get('results'):
            for uuid in request.data.get('uuid').split(','):
                if results.get('uuid') == uuid:
                    movies_list.append({'uuid':results.get('uuid'),
                                        'title':results.get('title'),
                                        'description':results.get('description'),
                                        'genres':results.get('genres')})

        instance = queryset.create(title=request.data.get('title'),
                                        description= request.data.get('description'),
                                        movies = movies_list)

        return Response(serializer_class(instance).data)

    def put(self, request, *args, **kwargs):
        instance = Collections.objects.get(id=kwargs.get('pk'))

        if request.data.get('title'):
            instance.title = request.data.get('title')

        if request.data.get('description'):
            instance.description = request.data.get('description')

        if request.data.get('uuid'):
            movies_api = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0','Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
            movies_api.text
            movies_api.headers['content-type']
            result = movies_api.json()
            
            res = list(eval(instance.movies))
            
            for results in result.get('results'):
                for uuid in request.data.get('uuid').split(','):
                    if results.get('uuid') == uuid:
                        res.append({'uuid':results.get('uuid'),
                                    'title':results.get('title'),
                                    'description':results.get('description'),
                                    'genres':results.get('genres')})

            instance.movies = res
            
        instance.save()

        return Response(CollectionsSerializers(instance).data)

    def delete(self, request, *args, **kwargs):

        instance = Collections.objects.get(id=kwargs.get('pk'))
        instance.delete()

        return Response(status=200)
