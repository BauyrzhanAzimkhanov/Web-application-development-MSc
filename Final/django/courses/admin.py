from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(UserProgress)
