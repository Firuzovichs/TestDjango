from django.contrib import admin
from .models import TestQuestion,ExcelUpload,TestResult
# Register your models here.
admin.site.register([ExcelUpload,TestResult])
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'is_correct_1', 'is_correct_2', 'is_correct_3', 'is_correct_4')  # Ko'rinadigan maydonlar
    search_fields = ('question',)  # Qidirish imkoniyati
    list_filter = ('is_correct_1', 'is_correct_2', 'is_correct_3', 'is_correct_4')  # Filterlar

admin.site.register(TestQuestion, TestQuestionAdmin)