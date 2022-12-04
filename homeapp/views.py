from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Note
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
@login_required
def homepage(request):
    return render(request,'homeapp/home.html',{"notes":Note.objects.all()})
@login_required
def add_note(request):
    if request.method=='POST':
        #print('jemannnnnnn')
        #print(request.user)
        f=Note(note_content=request.POST['name'],author=request.user)
        f.save()
    return redirect('notes-home')
class NoteListView(LoginRequiredMixin,ListView):
    model=Note
    template_name='homeapp/home.html'
    context_object_name='notes'
    ordering=['-date_posted']
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
class NoteDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Note
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class NoteDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Note
    success_url=reverse_lazy('notes-home')
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
def UpdateNote(request,pk):
    if Note.objects.get(id=pk).author==request.user:
        note_content=request.POST['note_content']
        author=request.user
        note=Note.objects.get(id=pk)
        note.note_content=note_content
        note.author=author
        note.save()
        return redirect('notes-home')
    else:
        return redirect('login')
