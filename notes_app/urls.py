from django.urls import path
from . import views
app_name = 'notes_app' 
urlpatterns = [
  path('', views.index, name='index'),
  path('notes/<int:id_note>', views.note, name='note'),
  path('notes/', views.notes, name='notes'),
  path('folders/', views.folders, name='folders'),
  path('folder/<int:id_folder>', views.folder, name='folder'),

  path('new_note', views.new_note, name='new_note'),
  path('new_folder', views.new_folder, name='new_folder'),
]