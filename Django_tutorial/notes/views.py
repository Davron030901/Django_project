from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import Http404
from .models import Note
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import NoteForm

from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteDeleteView(DeleteView):
    model = Note
    # fields = ['title', 'text']  # Modeldagi mavjud maydonlarni qo'shing
    template_name = 'notes/notes_delete.html'  # Sizning template faylingiz
    success_url = '/smart/notes'

class NoteUpdateView(UpdateView):
    model = Note
    # fields = ['title', 'text']  # Modeldagi mavjud maydonlarni qo'shing
    template_name = 'notes/note_form.html'  # Sizning template faylingiz
    success_url = '/smart/notes'
    form_class = NoteForm
class NoteCreateView(CreateView):
    model = Note
    # fields = ['title', 'text']  # Modeldagi mavjud maydonlarni qo'shing
    template_name = 'notes/note_form.html'  # Sizning template faylingiz
    success_url = '/smart/notes'
    form_class = NoteForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url='/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

# def list(request):
#     all_notes=Note.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note=Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes/notes_list.html', {'note': note})