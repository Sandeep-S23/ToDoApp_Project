from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from todo.models import Todo
from . serializers import ToDoSerializer, ToDoCompleteSerializer
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		# create new user
		try:
			data = JSONParser().parse(request)
			user = User.objects.create_user(data['username'], password=data['password'])
			user.save()
			token = Token.objects.create(user=user)
			return JsonResponse({"token":str(token)}, status=201)
		except IntegrityError:
			return JsonResponse({"error":"This username has already been taken, please choose a new username"}, status=400)


@csrf_exempt
def login(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		user = authenticate(request, username=data['username'], password=data['password'])
		if user is None:
			return JsonResponse({"error":"Could not login, please check username or password."}, status=400)
		else:
			try:
				token = Token.objects.get(user=user)
			except:
				token = Token.objects.create(user=user)		
			return JsonResponse({"token":str(token)}, status=200)



class TodoCompletedListView(generics.ListAPIView):
	serializer_class = ToDoSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by("-datecompleted") 		


class TodoListCreateView(generics.ListCreateAPIView):
	serializer_class = ToDoSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Todo.objects.filter(user=user, datecompleted__isnull=True).order_by("-created")

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ToDoSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Todo.objects.filter(user=user)

class TodoCompleteUpdateView(generics.UpdateAPIView):
	serializer_class = ToDoCompleteSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Todo.objects.filter(user=user)

	def perform_update(self, serializer):
		serializer.instance.datecompleted = timezone.now()
		serializer.save()

