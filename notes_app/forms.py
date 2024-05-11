from django import forms
from .models import Note, Folder

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['folder', 'title', 'content']
    labels = {'folder': 'Папка' , 'title': '', 'content': ''}
class FolderForm(forms.ModelForm):
  class Meta:
    model = Folder
    fields = ['name']
    labels = {'name': 'Название'}