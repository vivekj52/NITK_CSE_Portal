from django.http import HttpResponse
from django.template import loader
from .models import Faculty, Staff, ProjectStaff


def courses(request):
    template = loader.get_template('people.html')
    faculties = Faculty.objects.all()
    staffs = Staff.objects.all()
    project_staffs = ProjectStaff.objects.all()

    context = {'faculties': faculties,
               'staffs': staffs,
               'project_staffs': project_staffs}

    return HttpResponse(template.render(context, request))
