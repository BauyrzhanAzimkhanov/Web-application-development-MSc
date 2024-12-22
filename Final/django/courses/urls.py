from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import *
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter() 
router.register(r'users', UserViewSet) 
router.register(r'categories', CategoryViewSet) 
router.register(r'courses', CourseViewSet) 
router.register(r'enrollments', EnrollmentViewSet) 
router.register(r'lessons', LessonViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'payments', PaymentViewSet) 
router.register(r'quizzes', QuizViewSet) 
router.register(r'quiz_questions', QuizQuestionViewSet) 
router.register(r'user_progress', UserProgressViewSet) 


urlpatterns = [
    path('', include(router.urls)),
    path('render/courses/', CourseListView.as_view(), name='course_list'),
    path('render/courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('render/courses/new/', CourseCreateView.as_view(), name='course_create'),
    path('render/courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_update'),
    path('render/courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    path('render/categories/', CategoryListView.as_view(), name='category_list'),
    path('render/categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('render/categories/new/', CategoryCreateView.as_view(), name='category_create'),
    path('render/categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('render/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('render/enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('render/enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('render/enrollments/new/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('render/enrollments/<int:pk>/edit/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('render/enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),

    path('render/lessons/', LessonListView.as_view(), name='lesson_list'),
    path('render/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('render/lessons/new/', LessonCreateView.as_view(), name='lesson_create'),
    path('render/lessons/<int:pk>/edit/', LessonUpdateView.as_view(), name='lesson_update'),
    path('render/lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),

    path('render/payments/', PaymentListView.as_view(), name='payment_list'),
    path('render/payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('render/payments/new/', PaymentCreateView.as_view(), name='payment_create'),
    path('render/payments/<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment_update'),
    path('render/payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),

    path('render/quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('render/quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('render/quizzes/new/', QuizCreateView.as_view(), name='quiz_create'),
    path('render/quizzes/<int:pk>/edit/', QuizUpdateView.as_view(), name='quiz_update'),
    path('render/quizzes/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),

    path('render/quiz_questions/', QuizQuestionListView.as_view(), name='quiz_question_list'),
    path('render/quiz_questions/<int:pk>/', QuizQuestionDetailView.as_view(), name='quiz_question_detail'),
    path('render/quiz_questions/new/', QuizQuestionCreateView.as_view(), name='quiz_question_create'),
    path('render/quiz_questions/<int:pk>/edit/', QuizQuestionUpdateView.as_view(), name='quiz_question_update'),
    path('render/quiz_questions/<int:pk>/delete/', QuizQuestionDeleteView.as_view(), name='quiz_question_delete'),

    path('render/user_progress/', UserProgressListView.as_view(), name='user_progress_list'),
    path('render/user_progress/<int:pk>/', UserProgressDetailView.as_view(), name='user_progress_detail'),
    path('render/user_progress/new/', UserProgressCreateView.as_view(), name='user_progress_create'),
    path('render/user_progress/<int:pk>/edit/', UserProgressUpdateView.as_view(), name='user_progress_update'),
    path('render/user_progress/<int:pk>/delete/', UserProgressDeleteView.as_view(), name='user_progress_delete'),

    path('render/reviews/', ReviewListView.as_view(), name='review_list'),
    path('render/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('render/reviews/new/', ReviewCreateView.as_view(), name='review_create'),
    path('render/reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('render/reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

    path('render/users/', UserListView.as_view(), name='user_list'),
    path('render/users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('render/users/new/', UserCreateView.as_view(), name='user_create'),
    path('render/users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('render/users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
