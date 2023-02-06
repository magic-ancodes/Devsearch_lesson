from django.contrib import admin
from .models import Project, Review, Tag


admin.site.register([Project, Review, Tag])



