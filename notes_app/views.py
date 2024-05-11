from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Folder, Note
from .forms import NoteForm, FolderForm


# Create your views here.
def index(request):
  folders = Folder.objects.order_by('-data_updated')
  notes = Note.objects.order_by('-data_updated')
  context = {'folders': folders, 'notes': notes}
  return render(request, 'notes_app/index.html', context)
def note(request, id_note):
  note = Note.objects.get(id=id_note)
  if request.method != 'POST':
      form = NoteForm(instance=note)
  else:
      # Отправлены данные POST; обработать данные.
      form = NoteForm(instance=note, data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('notes_app:note', id_note=id_note)
  context = {'note': note, 'data_updated': note.data_updated, 'form': form}
  return render(request, 'notes_app/note.html', context)
def notes(request):
  return render(request, 'notes_app/notes.html', {'notes': Note.objects.order_by('-data_created')})

def folders(request):
  folders = Folder.objects.order_by('-data_updated')
  context = {'folders': folders}
  return render(request, 'notes_app/folders.html', context)
def folder(request, id_folder):
  folder = Folder.objects.get(id=id_folder)
  notes = folder.note_set.order_by('-data_updated')
  if request.method != 'POST':
      form = FolderForm(instance=folder)
  else:
      # Отправлены данные POST; обработать данные.
      form = FolderForm(instance=folder, data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('notes_app:folder', id_folder=id_folder)
  context = {'folder': folder, 'notes': notes, 'form': form}
  return render(request, 'notes_app/folder.html', context)

def new_note(request):
  """Определяет новую тему."""
  if request.method != 'POST':
      # Данные не отправлялись; создается пустая форма.
      form = NoteForm()
  else:
      # Отправлены данные POST; обработать данные.
      form = NoteForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('notes_app:index')
  # Вывести пустую или недействительную форму.
  context = {'form': form}
  return render(request, 'notes_app/new_note.html', context)

def new_folder(request):
  """Определяет новую тему."""
  if request.method != 'POST':
      # Данные не отправлялись; создается пустая форма.
      form = FolderForm()
  else:
      # Отправлены данные POST; обработать данные.
      form = FolderForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('notes_app:folders')
  # Вывести пустую или недействительную форму.
  context = {'form': form}
  return render(request, 'notes_app/new_folder.html', context)