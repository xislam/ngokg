from django.contrib import admin

# Register your models here.
from webapp.models import *


class RankLibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(RankLibrary, RankLibraryAdmin)


class LibraryFromNGOAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'description', 'files', 'created_date', 'edited_date')
    search_fields = ['name', 'description', 'files']


admin.site.register(LibraryFromNGO, LibraryFromNGOAdmin)


class RankLegislationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(RankLegislation, RankLegislationAdmin)


class LegislationAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'description', 'files')
    search_fields = ['name', 'description']


admin.site.register(Legislation, LegislationAdmin)


class QAAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']


admin.site.register(QA, QAAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('stars', 'text')
    search_fields = ['stars', 'text']


admin.site.register(Review, ReviewAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'text')
    search_fields = ['name', 'mail', 'text']


admin.site.register(Question, QuestionAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('dt', 'title', 'img', 'link', 'desc', 'site_name')
    search_fields = ['dt', 'title', 'img', 'link', 'desc', 'site_name']


admin.site.register(News, NewsAdmin)


