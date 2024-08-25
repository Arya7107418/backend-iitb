from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('instances/', views.CourseInstanceCreate.as_view(), name='course-instance-create'),
    path('instances/<int:year>/<int:semester>/', views.CourseInstanceList.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', views.CourseInstanceDetail.as_view(), name='course-instance-detail'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/delete/', views.CourseInstanceDelete.as_view(), name='course-instance-delete'),
]
