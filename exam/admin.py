from django.contrib import admin

from .models import ExamDetail, ExamIndex


class ExamDetailsInline(admin.StackedInline):
    model = ExamDetail
    extra = 1
    max_num = 1


class ExamIndexAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "slug", "university", "date"]}),
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }
    list_filter = ("university", "date")
    inlines = [ExamDetailsInline]


admin.site.site_header = "Exam Details Admin"
admin.site.site_title = "Exam Details Admin Portal"
admin.site.index_title = "Welcome to Exam Details Portal"
admin.site.register(ExamIndex, ExamIndexAdmin)
