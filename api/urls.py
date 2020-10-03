from django.urls import path
from . import views

urlpatterns = [
	#ToDos
	path('todos', views.TodoListCreateView.as_view()),
	path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyView.as_view()),
	path('todos/<int:pk>/complete', views.TodoCompleteUpdateView.as_view()),
	path('todos/completed', views.TodoCompletedListView.as_view()),

	#Auth
	path('signup', views.signup),
	path('login', views.login),
]