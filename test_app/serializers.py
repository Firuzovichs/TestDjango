from rest_framework import serializers
from .models import TestQuestion,TestResult,TimeModel
import random

class TestQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = TestQuestion
        fields = ['id', 'question', 'answers']

    def get_answers(self, obj):
        """Savolning barcha javoblarini tasodifiy tartibda qaytarish"""
        answers = [
            {"answer": obj.answer_1, "is_correct": obj.is_correct_1},
            {"answer": obj.answer_2, "is_correct": obj.is_correct_2},
            {"answer": obj.answer_3, "is_correct": obj.is_correct_3},
            {"answer": obj.answer_4, "is_correct": obj.is_correct_4},
        ]
        random.shuffle(answers)  # Javoblarni tasodifiy tartibda chiqarish
        return answers

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['id', 'fish', 'correct_answers', 'incorrect_answers', 'percentage','time_recorded','time']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeModel
        fields = ['__all__']