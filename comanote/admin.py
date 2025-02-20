from django.contrib import admin
from .models import Question, Answer
# Register your models here.

# 질문 검색기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)