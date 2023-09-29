from django.contrib import admin
from django.utils.safestring import mark_safe
from application.models import *


class InfoAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "profession", "age", "email", "habitation", "details", "get_photo"]
    list_display_links = ["name", "surname"]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Миниатюра'
    get_photo.allow_tags = True


class EducationAdmin(admin.ModelAdmin):
    list_display = ["organization", "profession", "start_date", "end_date", "details", "sort_key"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["company", "post", "start_date", "end_date", "details", "sort_key"]


class SkillsAdmin(admin.ModelAdmin):
    list_display = ["name_skill", "period", "url", "sort_key"]


class PetProjectsAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "photo", "description", "url", "sort_key"]


class CertificatesAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "sort_key"]


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["title", "url"]


class AddInformationAdmin(admin.ModelAdmin):
    list_display = ["content", "sort_key"]


admin.site.register(Info, InfoAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(PetProjects, PetProjectsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(AddInformation, AddInformationAdmin)
