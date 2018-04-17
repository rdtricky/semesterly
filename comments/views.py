from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from student.models import Student, PersonalTimetable
from student.utils import get_student, get_student_tts
from student.serializers import get_student_dict, StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from timetable.models import Semester
from django.contrib.auth.models import User
from comment.models import Comment

class CommentView(APIView):
    def get(self, request):

    def post(self, request):
        tt_id = request.data['tt_id']
        sem_name = request.data['sem_name']
        sem_year = request.data['sem_year']
        comment_str = request.data['comment_str']

        owner = get_student(request)
        tt = PersonalTimetable.objects.filter(student=student, pk=tt_id, school=school, semester=semester)
        tt.comments.add(Comment(comment_str)) #??? correct???
        # return


    def put(self, request):

    def delete(self, request):