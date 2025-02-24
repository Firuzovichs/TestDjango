from django.db import models
import pandas as pd
from io import BytesIO

class TestQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    is_correct_1 = models.BooleanField(default=False)
    answer_2 = models.CharField(max_length=255)
    is_correct_2 = models.BooleanField(default=False)
    answer_3 = models.CharField(max_length=255)
    is_correct_3 = models.BooleanField(default=False)
    answer_4 = models.CharField(max_length=255)
    is_correct_4 = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class ExcelUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Faylni saqlaymiz
        self.process_excel()  # Faylni qayta ishlashni chaqiramiz

    def process_excel(self):
        """Excel faylni o'qib, ma'lumotlarni TestQuestion modeliga saqlaydi."""
        if not self.file:
            return

        excel_file = self.file.open('rb')
        df = pd.read_excel(BytesIO(excel_file.read()))

        for _, row in df.iterrows():
            TestQuestion.objects.create(
                question=row['question'],
                answer_1=row['answer_1'], is_correct_1=row['is_correct_1'],
                answer_2=row['answer_2'], is_correct_2=row['is_correct_2'],
                answer_3=row['answer_3'], is_correct_3=row['is_correct_3'],
                answer_4=row['answer_4'], is_correct_4=row['is_correct_4'],
            )

class TestResult(models.Model):
    fish = models.CharField(max_length=2048)  # Foydalanuvchining FISH
    correct_answers = models.IntegerField(default=0)  # To'g'ri javoblar soni
    incorrect_answers = models.IntegerField(default=0)  # Noto'g'ri javoblar soni
    percentage = models.FloatField(default=0.0)  # To'g'ri javoblar foiz hisobida
    time_recorded = models.TimeField(auto_now_add=True)  # Faqat vaqtni saqlaydi
    time = models.TimeField(default="00:00")  # Yoki boshqa standart vaqt
    def calculate_percentage(self):
        """To'g'ri javoblar foizini hisoblash"""
        total = self.correct_answers + self.incorrect_answers
        if total > 0:
            self.percentage = (self.correct_answers / total) * 100
        else:
            self.percentage = 0
        self.save()

    def __str__(self):
        return f"{self.fish} - {self.percentage:.2f}% - {self.time}"