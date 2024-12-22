from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .permissions import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]




class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class CategoryListView(ListView): 
    model = Category 
    template_name = 'categories/category_list.html' 
    context_object_name = 'categories' 

class CategoryDetailView(DetailView): 
    model = Category 
    template_name = 'categories/category_detail.html' 
    context_object_name = 'category' 
    
class CategoryCreateView(CreateView): 
    model = Category 
    form_class = CategoryForm 
    template_name = 'categories/category_form.html' 
    success_url = reverse_lazy('category_list') 
    
class CategoryUpdateView(UpdateView): 
    model = Category 
    form_class = CategoryForm 
    template_name = 'categories/category_form.html' 
    success_url = reverse_lazy('category_list') 
    
class CategoryDeleteView(DeleteView): 
    model = Category 
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list') 

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'enrollments/enrollment_detail.html'
    context_object_name = 'enrollment'

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollments/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment_list')

class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson_list')

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    context_object_name = 'payments'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payments/payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'

class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz_list')

class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz_list')

class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quizzes/quiz_confirm_delete.html'
    success_url = reverse_lazy('quiz_list')

class QuizQuestionListView(ListView):
    model = QuizQuestion
    template_name = 'quiz_questions/quiz_question_list.html'
    context_object_name = 'quiz_questions'

class QuizQuestionDetailView(DetailView):
    model = QuizQuestion
    template_name = 'quiz_questions/quiz_question_detail.html'
    context_object_name = 'quiz_question'

class QuizQuestionCreateView(CreateView):
    model = QuizQuestion
    form_class = QuizQuestionForm
    template_name = 'quiz_questions/quiz_question_form.html'
    success_url = reverse_lazy('quiz_question_list')

class QuizQuestionUpdateView(UpdateView):
    model = QuizQuestion
    form_class = QuizQuestionForm
    template_name = 'quiz_questions/quiz_question_form.html'
    success_url = reverse_lazy('quiz_question_list')

class QuizQuestionDeleteView(DeleteView):
    model = QuizQuestion
    template_name = 'quiz_questions/quiz_question_confirm_delete.html'
    success_url = reverse_lazy('quiz_question_list')

class UserProgressListView(ListView):
    model = UserProgress
    template_name = 'user_progress/user_progress_list.html'
    context_object_name = 'user_progress_list'

class UserProgressDetailView(DetailView):
    model = UserProgress
    template_name = 'user_progress/user_progress_detail.html'
    context_object_name = 'user_progress'

class UserProgressCreateView(CreateView):
    model = UserProgress
    form_class = UserProgressForm
    template_name = 'user_progress/user_progress_form.html'
    success_url = reverse_lazy('user_progress_list')

class UserProgressUpdateView(UpdateView):
    model = UserProgress
    form_class = UserProgressForm
    template_name = 'user_progress/user_progress_form.html'
    success_url = reverse_lazy('user_progress_list')

class UserProgressDeleteView(DeleteView):
    model = UserProgress
    template_name = 'user_progress/user_progress_confirm_delete.html'
    success_url = reverse_lazy('user_progress_list')
