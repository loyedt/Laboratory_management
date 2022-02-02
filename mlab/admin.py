from django.contrib import admin
from .models import Tests, USER_RESULT, general_user, userprofile, bloodsugar,cholesterol,urinalysis
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
# admin.site.register(Tests)
admin.site.register(USER_RESULT)
admin.site.register(general_user)
# admin.site.register(userprofile)
# admin.site.register(bloodsugar)
# admin.site.register(cholesterol)

@admin.register(bloodsugar)
class bloodsugaradmin(admin.ModelAdmin):
    list_display =('userid','testdate','observedval','fasting')
    ordering = ('testdate',)
    search_fields = ('testdate',)
    list_filter = (
        ('testdate', DateRangeFilter),
        'testdate',
        'userid'
        )

@admin.register(cholesterol)
class cholesteroladmin(admin.ModelAdmin):
    list_display =('userid','testdate','triglycerides','hdl','ldl','totalcholesterol')
    ordering = ('testdate',)
    list_filter = (
        ('testdate', DateRangeFilter),
        'testdate',
        'userid'
        )

@admin.register(urinalysis)
class urinalysisadmin(admin.ModelAdmin):
    list_display =('userid','testdate','color','turpidity','ph','glucose','bilirubin','blood','protien','leukocyte')
    ordering = ('testdate',)
    list_filter = (
        ('testdate', DateRangeFilter),
        'testdate',
        'userid'
        )

@admin.register(userprofile)
class userprofileadmin(admin.ModelAdmin):
    list_display =('user','dob','phno','gender')
    list_filter = ('user','gender')

@admin.register(Tests)
class Testsadmin(admin.ModelAdmin):
    list_display =('name','price')

