from django.urls import path
from .views import UploadCSVFile, DownloadFilesView

urlpatterns = [
    path('upload/', UploadCSVFile.as_view(), name='upload-csv'),
    path("download/<str:request_id>/", DownloadFilesView.as_view()),
]
