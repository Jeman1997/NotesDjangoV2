from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns=[
path('',NoteListView.as_view(),name='notes-home'),
path('note/<int:pk>/',NoteDetailView.as_view(),name='note-detail'),
path('addnoteyo/',add_note,name='addnote'),
path('note/<int:pk>/updatenote/',UpdateNote,name='note-update'),
path('note/<int:pk>/delete/',NoteDeleteView.as_view(),name='note-delete'),
path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
