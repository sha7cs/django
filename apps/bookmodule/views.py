from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student, Department, Course, Address, Card,Student2
from django.db.models import Count
from django.shortcuts import redirect
from .forms import ImageForm
# Task 1
# def index(request):
#     return HttpResponse("Hello, world!")

# Task 2
# put this in the url to test (  http://127.0.0.1:8000/?name=shatha )
# def index(request):
#     name = request.GET.get("name") or "world!"  #add this line
#     return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name

# Task 3
# put this to test ( http://127.0.0.1:8000/index2/3/ ) You should see “value1 = 3” 
# def index2(request, val1 = 0): 
#     return HttpResponse("value1 = "+str(val1))


# # # Task 4
# # def index(request): 
# #     name = request.GET.get("name") or "world!"
# #     return render(request, "bookmodule/index.html")  
 
# # # Task 5
# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html" , {"name": name})  

# # # Task 7
# def viewbook(request, bookId):
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#     context = {'book':targetBook} # book is the variable name accessible by the template
#     return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html' )

def formatting(request):
    return render(request, 'bookmodule/formatting.html' )

def listing(request):
    return render(request, 'bookmodule/listing.html' )

def tables(request):
    return render(request, 'bookmodule/tables.html' )

def search(request):
    if request.method == "GET":
        return render(request, 'bookmodule/listbbooks.html')
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/listbbooks.html', {'books':newBooks})
 

    # return render(request, 'bookmodule/listbbooks.html' )

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
 
from .models import Book

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') # <- multiple objects
    # mybooks = Book.objects.all() # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 50)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def task1(request):
    books = Book.objects.filter(Q(price__lte=80)) # have price less than or equal 80 
    return render(request,'bookmodule/Task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains="co") | Q(author__icontains="co"))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(
            Q(title__icontains="co") | Q(author__icontains="co")
        )
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')  
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books = Count('id'),
        total_price =Sum('price'),
        average_price =Avg('price'),
        max_price =Max('price'),
        min_price =Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})


def task7(request):
    stats = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'stats': stats})

def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request,'bookmodule/lab9_task1.html',{'departments':departments})

def lab9_task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request,'bookmodule/lab9_task2.html',{'courses':courses})

def lab9_task3(request):
    departments = Department.objects.annotate(min_student_id=Min('student__id'))
    return render(request,'bookmodule/lab9_task3.html',{'departments':departments})

def lab9_task4(request):
  departments = ( Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count'))
  return render(request,'bookmodule/lab9_task4.html',{'departments':departments})

def lab9_part1_listbooks(request):
    books = Book.objects.all
    return render(request, 'bookmodule/lab9_list.html',{'books':books})

def lab9_part1_addbook(request):
    if request.method =='POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price,edition=edition)

        return redirect('lab9-list')  

    return render(request, 'bookmodule/lab9_add.html')


def lab9_part1_editbook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        book.title = title
        book.author = author
        book.price = price
        book.edition = edition
        book.save()

        return redirect('lab9-list')
    
    return render(request, 'bookmodule/lab9_edit.html',{'book':book})


def lab9_part1_deletebook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        book.delete()
        return redirect('lab9-list')  

    return render(request, 'bookmodule/lab9_delete.html',{'book':book})   


from .forms import Book_form,Student1Form,Student2Form


def lab9_part1_add_form(request):
    if request.method == 'POST':
        form = Book_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9-list')
    else:
        form = Book_form()

    return render(request, 'bookmodule/lab9_add_form.html', {'form': form})


def lab9_part1_edit_form(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = Book_form(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9-list')
    else:
        form = Book_form(instance=book)

    return render(request, 'bookmodule/lab9_edit_form.html', {'form': form, 'book': book})

from .models import Student1

def lab11_list(request):
    students = Student1.objects.all
    return render(request,'students/stds-list.html',{'students':students})

def lab11_add(request):
    if request.method == 'POST':
        form = Student1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab11-list')
    else:
        form = Student1Form()

    return render(request, 'students/add-student.html', {'form': form})

def lab11_edit(request, std_id):
    student = Student1.objects.get(id=std_id)

    if request.method == 'POST':
        form = Student1Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab11-list')
    else:
        form = Student1Form(instance=student)
    return render(request, 'students/edit-student.html', {'form': form, 'book': student})

def lab11_delete(request,std_id):
    student = Student1.objects.get(id=std_id)
    if request.method =='POST':
        student.delete()
        return redirect('lab11-list')  
    return render(request, 'students/delete-students.html',{'student':student})   


# the same lab but task 2
def lab12_list(request):
    students = Student2.objects.all()
    return render(request, 'students/stds2-list.html', {'students': students})

def lab12_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab12-list')
    else:
        form = Student2Form()

    return render(request, 'students/add-student2.html', {'form': form})

def lab12_edit(request, std_id):
    student = Student2.objects.get(id=std_id)

    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab12-list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'students/edit-student2.html', {'form': form, 'student': student})

def lab12_delete(request, std_id):
    student = Student2.objects.get(id=std_id)
    if request.method == 'POST':
        student.delete()
        return redirect('lab12-list')
    return render(request, 'students/delete-students2.html', {'student': student})


from .models import Images
def list_images(request):
    images = Images.objects.all()
    return render(request, 'students/list-images.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image-list')
    else:
        form = ImageForm()

    return render(request, 'students/add-image.html', {'form': form})