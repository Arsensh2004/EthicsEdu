from django.contrib import admin
from .models import Lesson, Question, Answer

# Позволяет добавлять ответы прямо при создании вопроса
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

# Отображение вопросов с вложенными ответами
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

# Регистрируем модели
admin.site.register(Lesson)           # ✅ теперь уроки тоже доступны в админке
admin.site.register(Question, QuestionAdmin)
