from django.contrib import admin
from .models import TestQuestion,ExcelUpload,TestResult,TimeModel
from django.http import HttpResponse
import pandas as pd

# Register your models here.
admin.site.register([ExcelUpload,TimeModel])
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'is_correct_1', 'is_correct_2', 'is_correct_3', 'is_correct_4')
    search_fields = ('question',)
    list_filter = ('is_correct_1', 'is_correct_2', 'is_correct_3', 'is_correct_4')

    # Excelga yuklab olish uchun action
    actions = ['export_as_excel']

    def export_as_excel(self, request, queryset):
        # Ma'lumotlarni DataFramega o'girish
        data = list(queryset.values('id', 'question', 'is_correct_1', 'is_correct_2', 'is_correct_3', 'is_correct_4'))
        df = pd.DataFrame(data)

        # Excel faylini yaratish
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=test_questions.xlsx'

        # DFni Excelga yozish
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='TestQuestions')

        return response

    export_as_excel.short_description = "Tanlangan savollarni Excelga yuklab olish"

admin.site.register(TestQuestion, TestQuestionAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'fish', 'correct_answers', 'incorrect_answers', 'percentage', 'time_recorded', 'time')
    search_fields = ('fish',)
    list_filter = ('percentage', 'time_recorded')

    actions = ['export_results_as_excel']

    def export_results_as_excel(self, request, queryset):
        """Test natijalarini Excelga yuklash"""
        data = list(queryset.values('id', 'fish', 'correct_answers', 'incorrect_answers', 'percentage', 'time_recorded', 'time'))
        df = pd.DataFrame(data)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=test_results.xlsx'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='TestResults')

        return response

    export_results_as_excel.short_description = "Tanlangan natijalarni Excelga yuklab olish"

admin.site.register(TestResult, TestResultAdmin)