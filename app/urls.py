
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView



def hello_view(request):
    return JsonResponse({'message': 'hello world!'})

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('authentication.urls')),


]
