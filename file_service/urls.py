from django.urls import path
from .views import UploadCSVFile, DownloadFilesView

urlpatterns = [
    path('v1/upload/', UploadCSVFile.as_view(), name='upload-csv'),
    path("v1/download/<str:request_id>/", DownloadFilesView.as_view()),
]
