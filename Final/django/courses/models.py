from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    groups = models.ManyToManyField( 
        Group,
        related_name='custom_user_set', # Change related_name to avoid conflict
        blank=True, 
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'), 
        related_query_name='user', 
    ) 
    user_permissions = models.ManyToManyField( 
        Permission, 
        related_name='custom_user_set', # Change related_name to avoid conflict 
        blank=True, 
        help_text=('Specific permissions for this user.'), 
        related_query_name='user', 
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_instructor': True})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
    
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.course.title}"
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username}"
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name = "QuizQuestion"
        verbose_name_plural = "QuizQuestions"


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.IntegerField()
    quiz_scores = models.JSONField()

    def __str__(self):
        return f"Progress of {self.user.username} in {self.course.title}"
    
    class Meta:
        verbose_name = "UserProgress"
        verbose_name_plural = "UserProgress"
