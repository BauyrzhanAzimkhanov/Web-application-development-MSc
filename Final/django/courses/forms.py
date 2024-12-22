from django import forms
from .models import User, Category, Course, Enrollment, Lesson, Review, Payment, Quiz, QuizQuestion, UserProgress


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_student', 'is_instructor']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'category', 'instructor']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'status']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'video_url']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['course', 'user', 'rating', 'comment']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'amount', 'status']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['course', 'title', 'total_marks']


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['quiz', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']


class UserProgressForm(forms.ModelForm):
    class Meta:
        model = UserProgress
        fields = ['user', 'course', 'completed_lessons', 'quiz_scores']

