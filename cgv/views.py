import json

from django.http     import JsonResponse
from django.views    import View
from cgv.models import Actor, Movie

# views

class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth']
        )
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()

        result = []
        for actor in actors:
            actors_movies = actor.movies.all()
            actors_movies_list = []
            for actors_movie in actors_movies:
                actors_movies_info = {
                    'movie' : actors_movie.title
                }
                actors_movies_list.append(actors_movies_info)

            actors_info = {
                'first_name' : actor.first_name,
                'last_name' : actor.last_name,
                'date_of_birth' : actor.date_of_birth,
                'actors_movies' : actors_movies_list
            }
            result.append(actors_info)

        return JsonResponse({'result':result}, status=201)

class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title=data['title'],
            release_date=data['release_date'],
            running_time=data['running_time']
        )
        return JsonResponse({'message':'created'}, status=201)
    
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            movie_lns = movie.actors.all()
            movie_ln_list = []
            for movie_ln in movie_lns:
                actor_info = {
                    'actor' : movie_ln.actor
                }
                movie_ln_list.append(actor_info)
            movie_info = {
                'title' : movie.title,
                'release_date' : movie.release_date,
                'running_time' : movie.running_time,
                'movie_lns' : movie_ln_list
            }
            result.append(movie_info)

        return JsonResponse({'result':result}, status=201)

## m to m 이라서 쓸 필요가 없음
# class Actos_moviesView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         actor = Actor.objects.get(last_name=data['actor'])
#         movie = Movie.objects.get(title=data['movie'])
#         Actors_movies.objects.create(
#             actor = actor,
#             movie = movie
#         )

#         return JsonResponse({'message':'created'}, status=201)

#     def get(self, request):
#         actors_movies = Actors_movies.objects.all()

#         result = []
#         for actors_movie in actors_movies:
#             actors_movie_info = {
#                 'actor' : actors_movie.actor.last_name,
#                 'movie' : actors_movie.movie.title
#             }
#             result.append(actors_movie_info)
#         return JsonResponse({'result':result}, status=200)






