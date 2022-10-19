from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/', JobDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', JobUpdateView.as_view(), name="post_edit"),
    path('post/new/', JobCreateView.as_view(), name="post_new"),
    path('post/<int:pk>', JobDetailView.as_view(), name="post_detail"),
    path('', JobListView.as_view(), name='home')
]
