from django.urls import path
from . import views

urlpatterns = [
    # path('ddetails/', views.ddetails, name='ddetails'),
    path('patients/', views.patient, name='patient'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('emergencys/', views.emergencys, name='emergencys'),
    path('emergency/', views.emergency,  name='emergency'),
    path('patient/edit/<int:id>', views.edits, name='edit'),
    path('patient/details/<int:id>', views.details, name='detail'),
    path('patient/delete/<int:id>', views.delete, name='delete')

]