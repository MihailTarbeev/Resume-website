from http.client import HTTPResponse

from django.shortcuts import render

from application.models import *


def index(request):
    data = {
        "info": Info.objects.first(),
        "education": Education.objects.all(),
        "experience": Experience.objects.all(),
        "skills": Skills.objects.all(),
        "pet_projects": PetProjects.objects.all(),
        "certificates": Certificates.objects.all(),
        "social_media": SocialMedia.objects.all(),
        "add_information": AddInformation.objects.all(),
        "list_234": [2, 3, 4]
    }
    return render(request, 'application/index.html', context=data)

