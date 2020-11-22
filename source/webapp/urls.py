from django.conf.urls.static import static
from django.urls import path

from main import settings
from webapp import views
from webapp.views import QuestionView, ReviewView, SearchView

urlpatterns = [
    path('rank_library_list/', views.rank_library_list),
    path('rank_library_detail/<int:pk>/', views.rank_library_detail),
    path('library_from_nko_list/', views.library_from_nko_list),
    path('library_from_nko_detail/<int:pk>/', views.library_from_nko_detail),
    path('rank_legislation_list/', views.rank_legislation_list),
    path('rank_legislation_detail/<int:pk>/', views.rank_legislation_detail),
    path('legislation_list/', views.legislation_list),
    path('legislation_detail/<int:pk>/', views.legislation_detail),
    path('qa_list/', views.qa_list),
    path('qa_detail/<int:pk>/', views.qa_detail),
    path('questions/', QuestionView.as_view(), name='question_create'),
    path('review/', ReviewView.as_view(), name='review_create'),
    path('search/', SearchView.as_view(), name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)