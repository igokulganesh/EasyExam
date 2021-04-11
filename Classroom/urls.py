from django.urls import path

from .views import Students, Teachers, Classroom

urlpatterns = [

	# For Classroom
	path('', Classroom.home, name='home'),
	path('dashboard', Classroom.dashboard, name='dashboard'),
	path('<int:class_id>/view_class', Classroom.view_class, name='view_class'),

	path('signup', Classroom.signup, name='signup'),
	path('login', Classroom.login, name='login'),
	path('logout', Classroom.logout, name='logout'),
	
	# For Students 
	path('join_class', Students.join_class, name='join_class'),

	# For Teachers 
	path('create_class', Teachers.create_class, name='create_class'),
	path('<int:class_id>/create_test', Teachers.create_test, name='create_test'),
	path('<int:test_id>/view_test', Teachers.view_test, name='view_test'),

]