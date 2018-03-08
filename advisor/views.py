from django.http import HttpResponse
from student.models import Student, PersonalTimetable
from student.utils import get_student
from student.serializers import get_student_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from timetable.models import Semester
from django.contrib.auth.models import User


class AdvisorView(APIView):
    def post(self, request):
        """ Add an advisor by email """
        try:
            tt_id = request.data['tt_id']
            sem_name = request.data['sem_name']
            sem_year = request.data['sem_year']
            advisor_email = request.data['advisor_email']

            student = get_student(request)
            semester = Semester.objects.get(name=sem_name, year=sem_year)
            school = request.subdomain

            output = []
            advisors_list = list(User.objects.filter(email=advisor_email))
            for advisor in advisors_list:
                timetable = PersonalTimetable.objects.get(student=student, pk=tt_id, school=school, semester=semester)
                if timetable:
                    advisor_obj = Student.objects.get(user=advisor)
                    timetable.advisors.add(advisor_obj)
                    output.append(get_student_dict(school, advisor_obj, semester))
            return Response({'advisors_added': output}, status=200)
        except KeyError:
            return Response({'reason': 'incorrect request format'}, status=404)
