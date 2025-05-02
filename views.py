from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, Lesson
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import TestResult
from django.contrib.auth.decorators import login_required
def quiz_start(request):
    return render(request, 'ethics/quiz_start.html')
def home(request):
    lessons = Lesson.objects.all().order_by('-created_at')
    return render(request, 'ethics/home.html', {'lessons': lessons})
def quiz_run(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected and Answer.objects.filter(id=selected, is_correct=True).exists():
                score += 1
        return redirect('quiz_result') + f'?score={score}&total={questions.count()}'
    return render(request, 'ethics/quiz_run.html', {'questions': questions})

def quiz_result(request):
    score = request.GET.get('score')
    total = request.GET.get('total')
    return render(request, 'ethics/quiz_result.html', {'score': score, 'total': total})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'ethics/lesson_detail.html', {'lesson': lesson})

def quiz_run(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected and Answer.objects.filter(id=selected, is_correct=True).exists():
                score += 1
        return redirect(f'/quiz/result/?score={score}&total={questions.count()}')
    return render(request, 'ethics/quiz_run.html', {'questions': questions})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ethics/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'ethics/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def quiz_run(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected and Answer.objects.filter(id=selected, is_correct=True).exists():
                score += 1

        # Сохраняем результат
        TestResult.objects.create(
            user=request.user,
            score=score,
            total=questions.count()
        )

        return redirect(f'/quiz/result/?score={score}&total={questions.count()}')
    return render(request, 'ethics/quiz_run.html', {'questions': questions})

@login_required
def profile(request):
    results = TestResult.objects.filter(user=request.user).order_by('-date')
    return render(request, 'ethics/profile.html', {'results': results})
def about(request):
    return render(request, 'ethics/about.html')

def literature(request):
    return render(request, 'ethics/literature.html')

def videos(request):
    return render(request, 'ethics/videos.html')

def articles(request):
    return render(request, 'ethics/articles.html')