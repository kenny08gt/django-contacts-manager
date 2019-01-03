from django.urls import path

from . import views

app_name = 'manage_contacts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add_person', views.AddPersonView.as_view(), name='add_person'),
    path('add_person', views.add_person, name='add_person_save'),

    path('add_contact', views.AddContactView.as_view(), name='add_contact'),
    path('add_contact', views.add_contact, name='add_contact_save'),
]