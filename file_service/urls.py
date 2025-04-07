from django.urls import path
from .views import UploadCSVFile, DownloadFilesView
from .health import HealthCheckView

urlpatterns = [
    path('v1/upload/', UploadCSVFile.as_view(), name='upload-csv'),
    path("v1/download/<str:request_id>/", DownloadFilesView.as_view()),
    path('health/', HealthCheckView.as_view(), name='health'),
]
