from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, PaperCreateView, PaperUpdateView, PaperDeleteView, PaperDetailView, PaperListView

urlpatterns = [
    path('post/<int:pk>/delete/', JobDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', JobUpdateView.as_view(), name="post_edit"),
    path('post/new/', JobCreateView.as_view(), name="post_new"),
    path('post/<int:pk>', JobDetailView.as_view(), name="post_detail"),
    path('post/paper_new', PaperCreateView.as_view(), name="paper_new"),
    path('post/<int:pk>/edit_paper/', PaperUpdateView.as_view(), name="post_paper_edit"),
    path('post/<int:pk>/delete_paper/', PaperDeleteView.as_view(), name="post_paper_delete"),
    path('paper_post/<int:pk>', PaperDetailView.as_view(), name="post_paper_detail"),
    path('paper/', PaperListView.as_view(), name='paper_home'),
    path('', JobListView.as_view(), name='home')
]
