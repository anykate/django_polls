from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, api_views


app_name = 'polls'

urlpatterns = [
    # Regular Django Views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/',
         views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # API views
    path('polls/api/questions/', api_views.QuestionList.as_view()),
    path('api/questions/<int:pk>/',
         api_views.QuestionDetail.as_view()),
    path('api/choices/<int:pk>/', api_views.ChoiceDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
