from django.contrib import admin
from .models import Blog, Title ,Contact, About,Welcome

# Register your models here.
admin.site.register(Title)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Welcome)