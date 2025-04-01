from django.urls import path
from .views import UploadCSVFile

urlpatterns = [
    path('upload/', UploadCSVFile.as_view(), name='upload-csv'),
]
