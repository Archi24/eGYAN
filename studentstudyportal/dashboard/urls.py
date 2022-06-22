from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('notes/',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
     path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
     path('homework/',views.homework,name="homework"),
      path('update_homework/<int:pk>',views.update_homework,name="update-homework"),
       path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
        path('youtu/',views.youtube,name="youtubes"),
        path('todos/',views.todo,name="todos"),
        path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
         path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),
         path('books/',views.books,name="books"),
           path('dictionaries/',views.dictionary,name="dict"),
                      path('wikis/',views.wiki,name="wikis"),
          path('conversions/',views.conversion,name="conversions"),
         
]
#      path('update_homework/<int:pk>',views.update_homework,name="update-homework"),
#       path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
# ]


  