from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Question

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(QuestionAdmin)