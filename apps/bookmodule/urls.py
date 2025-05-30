from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name="books.links"),
    path('html5/text/formatting', views.formatting, name="books.formatting"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/tables', views.tables, name="books.tabls"),
    path('search/', views.search, name= "books.search"),
    path('booklist/', views.simple_query, name= "books.query"),
    path('booklist2/', views.complex_query, name= "books.query.complex"),
    path('lab8/task1/', views.task1, name= "task1"),
    path('lab8/task2/', views.task2, name='task2'),#lab 8
    path('lab8/task3/', views.task3, name='task3'),#lab 8
    path('lab8/task4/', views.task4, name='task4'),#lab 8
    path('lab8/task5/', views.task5, name='task5'),#lab 8
    path('lab8/task7/', views.task7, name='task7'),#lab 8
    path('lab9/task1', views.lab9_task1 ,name='lab9-task1'),
    path('lab9/task2', views.lab9_task2 ,name='lab9-task2'),
    path('lab9/task3', views.lab9_task3 ,name='lab9-task3'),
    path('lab9/task4', views.lab9_task4 ,name='lab9-task4'),
    path('lab9_part1/list', views.lab9_part1_listbooks ,name='lab9-list'),
    path('lab9_part1/add', views.lab9_part1_addbook ,name='lab9-add'),
    path('lab9_part1/edit/<int:book_id>', views.lab9_part1_editbook ,name='lab9-edit'),
    path('lab9_part1/delete/<int:book_id>', views.lab9_part1_deletebook ,name='lab9-delete'),
    path('lab9_part1/add-form/', views.lab9_part1_add_form ,name='lab9-add-form'),
    path('lab9_part1/edit-form/<int:book_id>', views.lab9_part1_edit_form ,name='lab9-edit-form'),
    #lab11
    path('lab11/list/students', views.lab11_list ,name='lab11-list'),
    path('lab11/add/', views.lab11_add ,name='lab11-add'),
    path('lab11/edit/<int:std_id>', views.lab11_edit ,name='lab11-edit'),
    path('lab11/delete/<int:std_id>', views.lab11_delete ,name='lab11-delete'),
    #lab 11 task 2
    path('lab12/list/students', views.lab12_list, name='lab12-list'),
    path('lab12/add/', views.lab12_add, name='lab12-add'),
    path('lab12/edit/<int:std_id>', views.lab12_edit, name='lab12-edit'),
    path('lab12/delete/<int:std_id>', views.lab12_delete, name='lab12-delete'),
    #lab 11 task 3
    path('upload/', views.upload_image, name='image-upload'),
    path('images/', views.list_images, name='image-list'),
    # lab 12 
    path('login/', views.user_login, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

]