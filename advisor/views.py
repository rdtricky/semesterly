# Copyright (C) 2017 Semester.ly Technologies, LLC
#
# Semester.ly is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Semester.ly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from student.models import Student, PersonalTimetable
from student.serializers import get_student_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from timetable.models import Semester
from django.contrib.auth.models import User


class AdvisorView(APIView):
    def get(self, request, sem_name, sem_year, email):
        """
        Search an advisor by email.
        Return student advisor user object if valid email, else return 404
        """
        try:
            student = User.objects.filter(email=email)[0]

            semester = Semester.objects.get(name=sem_name, year=sem_year)
            response = {
                'student': student.email  # handles if not student too
            }
            # if advisor not found, empty
            return Response(response, status=200)
        except KeyError:
            return HttpResponse(status=404)  # malformed request

    # def post(self, request):
    #         name = request.data['name']
    #         sem_name = request.data['sem_name']
    #         year = request.data['year']
    #         viewer_email = request.data['viewer_email']
    #
    #         semester = Semester.objects.get(name=sem_name, year=year)
    #         student = Student.objects.get(user=request.user)
    #         school = request.subdomain
    #         to_add_viewer = PersonalTimetable.objects.filter(student=student, name=name, school=school, semester=semester)
    #         viewer = Student.objects.get(id=1)
    #         print(to_add_viewer)
    #         print(viewer)
    #         if viewer:
    #             to_add_viewer.viewers.add(viewer_email)
    #             print('Success!')
    #             return HttpResponse(status=200)
    #         else:
    #             # TODO: Send Error message that viewer is not found
    #             print('Fail :(')
    #             return HttpResponse(status=404)
