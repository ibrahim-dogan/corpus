from django.conf.urls import url
from .views import UploadFile, CleanWithParameters

urlpatterns = [
    url('upload/', UploadFile.as_view(), name='file-upload'),
    url('cleaning/', CleanWithParameters.as_view(), name='cleaning'),

]
