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
from helpers.mixins import ValidateSubdomainMixin, RedirectToSignupMixin
from helpers.decorators import validate_subdomain


class CommentView(APIView):
    def get(self, request, sem_name, sem_year, tt_id ):
        try:
            sem, _ = Semester.objects.get_or_create(name=sem_name, year=sem_year)
            student = Student.objects.get(user=request.user)
            timetable = student.personaltimetable_set.filter(
                     school=request.subdomain, semester=sem, pk=tt_id)
            commments = timetable.comments.all()
            return Response({'comments', comments}, status=200)
        except:
            return Response({'?', []}, status=404)

    def post(self, request):
        try:
            tt_id = request.data['tt_id']
            sem_name = request.data['sem_name']
            sem_year = request.data['sem_year']
            comment_str = request.data['comment_str']

            owner = get_student(request)
            tt = PersonalTimetable.objects.filter(student=student, pk=tt_id, school=school, semester=semester)
            comment = Comment(comment_str)
            tt.comments.add(comment)
            return Response({'comment_added', comment}, status=200)
        except:
            return Response({'?', []}, status=404)


    def put(self, request):

    def delete(self, request):