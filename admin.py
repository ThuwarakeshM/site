from django.contrib import admin
from .models import Query, Blog, Tag, Section, Author

# Register your models here.
admin.site.register(Query)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(Author)