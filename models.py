from django.db import models
from django.contrib.auth.models import User

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    score = models.PositiveIntegerField(verbose_name="Правильных ответов")
    total = models.PositiveIntegerField(verbose_name="Всего вопросов")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"{self.user.username} — {self.score}/{self.total} ({self.date.date()})"


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
class Question(models.Model):
    text = models.CharField(max_length=300, verbose_name="Текст вопроса")

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name="Вариант ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return f"{self.text} ({'✔' if self.is_correct else '✘'})"

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    score = models.PositiveIntegerField(verbose_name="Правильных ответов")
    total = models.PositiveIntegerField(verbose_name="Всего вопросов")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"{self.user.username} — {self.score}/{self.total} ({self.date.date()})"