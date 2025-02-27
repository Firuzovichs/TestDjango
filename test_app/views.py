from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TestQuestion,TestResult,TimeModel
from .serializers import TestQuestionSerializer,TestResultSerializer,TimeSerializer
import random
from rest_framework import generics

class RandomTestQuestionsAPIView(APIView):
    def get(self, request):
        # TestQuestion modelidan barcha savollarni olish
        questions = list(TestQuestion.objects.all())

        # Agar 30 ta yoki undan ko‘p savol bo‘lsa, tasodifiy 30 tasini tanlab olamiz
        if len(questions) > 30:
            questions = random.sample(questions, 30)

        # Serializatsiya qilish
        serializer = TestQuestionSerializer(questions, many=True)

        return Response(serializer.data)
class TestResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class TimeApiView(APIView):
    def get(self, request):
        # TestQuestion modelidan barcha savollarni olish
        questions = list(TimeModel.objects.all())

        # Serializatsiya qilish
        serializer = TimeSerializer(questions, many=True)