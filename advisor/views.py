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
from rest_framework.views import APIView
from timetable.models import Semester

class AdvisorView(APIView):
     def post(self, request):
            name = request.data['name']
            sem_name = request.data['sem_name']
            year = request.data['year']
            viewer_email = request.data['viewer_email']

            semester = Semester.objects.get(name=sem_name, year=year)
            student = Student.objects.get(user=request.user)
            school = request.subdomain
            to_add_viewer = PersonalTimetable.objects.filter(student=student, name=name, school=school, semester=semester)
            viewer = Student.objects.get(id=1)
            print(to_add_viewer)
            print(viewer)
            if viewer:
                to_add_viewer.viewers.add(viewer_email)
                print('Success!')
                return HttpResponse(status=200)
            else:
                # TODO: Send Error message that viewer is not found
                print('Fail :(')
                return HttpResponse(status=404)

#      def get(self, request):
#              """
#              Get all Users who match the query (name) so that the user can add them as a
#              viewer to their timetable
#              """
#              student = Student.objects.get(user=request.user)