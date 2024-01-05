from .views import addnew, edit, update, destroy, index
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('addnew', addnew, name='addnew'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='delete'),
]
