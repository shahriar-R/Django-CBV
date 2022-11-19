from django.urls import path, include


app_name = 'api-v1'

urlpatterns = [

    path('registration/',views.RegistrationApiView.as_view(), name="registration"),
    
]