from django.urls import path
from . import views

urlpatterns = [
    # path('/', name='landing_quiz'),
    path('quiz/<int:question_id>/', views.quiz, name='quiz')
]