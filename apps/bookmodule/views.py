from django.shortcuts import render
from django.http import HttpResponse

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



