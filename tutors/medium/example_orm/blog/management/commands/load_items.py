from django.core.management import BaseCommand
from django.utils import timezone
from blog.models import Blog, Author, Entry


class Command(BaseCommand):
    def handle(self, *args, **options):
        blogs = [
            Blog(name='Blog{}'.format(i), tagline='This is Tagline {}'.format(i))
            for i in range(1, 10000)
        ]
        Blog.objects.bulk_create(blogs)

        authors = [
            Author(name='Author{}'.format(i), email='author{}@example.com'.format(i))
            for i in range(1, 10000)
        ]
        Author.objects.bulk_create(authors)

        entries = [
            Entry(
                blog_id=i,
                headline="Headline{}".format(i),
                pub_date=timezone.now()
                ) 
            for i in range(1, 10000)
        ]
        Entry.objects.bulk_create(entries)

        for entry in Entry.objects.all():
            entry.authors.add(*list(Author.objects.all()[0:100]))