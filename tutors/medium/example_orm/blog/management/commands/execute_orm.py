
from django.core.management import BaseCommand
from django.utils import timezone
from blog.models import Blog, Author, Entry
from blog.decorators import query_debugger
import threading

def process(books: list, entries:list):
    for entry in entries:
        books.append({'name': entry.blog.name, 'author': entry.authors.all().values_list('name', flat=True)})


@query_debugger
def book_list_multithread():
    
    queryset = Entry.objects.all()
        # select_related('blog').prefetch_related('authors').\
        # only('blog__name', 'authors__name')
    # print(queryset.explain())
 
    books = []
    threads = []
    limit = 100
    page = 1
    offset = 0
    while page <= queryset.count() / limit:
        x = threading.Thread(target=process, args=(books, queryset[offset:offset+limit], ))
        threads.append(x)
        offset += limit
        page += 1
        x.start()
        x.join()
    return books

@query_debugger
def book_list():
    queryset = Entry.objects.all()
        # select_related('blog').prefetch_related('authors').\
        # only('blog__name', 'authors__name')
    books = []
    for entry in queryset:
        # authors = [author.name for author in entry.authors.all()]
        books.append({'name': entry.blog.name, 'author': entry.authors.all().values_list('name', flat=True)})
    return books


class Command(BaseCommand):
    def handle(self, *args, **options):
        book_list_multithread()
        # book_list()
