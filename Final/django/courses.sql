BEGIN;
--
-- Create model Category
--
CREATE TABLE "courses_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(200) NOT NULL, "description" text NOT NULL);
--
-- Create model Course
--
CREATE TABLE "courses_course" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "price" numeric(6, 2) NOT NULL, "created_at" timestamp with time zone NOT NULL, "category_id" bigint NOT NULL);
--
-- Create model Lesson
--
CREATE TABLE "courses_lesson" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "content" text NOT NULL, "video_url" varchar(200) NULL, "course_id" bigint NOT NULL);
--
-- Create model Quiz
--
CREATE TABLE "courses_quiz" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "total_marks" integer NOT NULL, "course_id" bigint NOT NULL);
--
-- Create model QuizQuestion
--
CREATE TABLE "courses_quizquestion" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "question_text" text NOT NULL, "option_a" varchar(200) NOT NULL, "option_b" varchar(200) NOT NULL, "option_c" varchar(200) NOT NULL, "option_d" varchar(200) NOT NULL, "correct_option" varchar(1) NOT NULL, "quiz_id" bigint NOT NULL);
--
-- Create model User
--
CREATE TABLE "courses_user" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL, "is_student" boolean NOT NULL, "is_instructor" boolean NOT NULL);
CREATE TABLE "courses_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" bigint NOT NULL, "group_id" integer NOT NULL);
CREATE TABLE "courses_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" bigint NOT NULL, "permission_id" integer NOT NULL);
--
-- Create model Review
--
CREATE TABLE "courses_review" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "rating" integer NOT NULL, "comment" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "course_id" bigint NOT NULL, "user_id" bigint NOT NULL);
--
-- Create model Payment
--
CREATE TABLE "courses_payment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "amount" numeric(6, 2) NOT NULL, "payment_date" timestamp with time zone NOT NULL, "status" varchar(20) NOT NULL, "user_id" bigint NOT NULL);
--
-- Create model Enrollment
--
CREATE TABLE "courses_enrollment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "enrollment_date" timestamp with time zone NOT NULL, "status" varchar(20) NOT NULL, "course_id" bigint NOT NULL, "user_id" bigint NOT NULL);
--
-- Add field instructor to course
--
ALTER TABLE "courses_course" ADD COLUMN "instructor_id" bigint NOT NULL CONSTRAINT "courses_course_instructor_id_5b0643dc_fk_courses_user_id" REFERENCES "courses_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "courses_course_instructor_id_5b0643dc_fk_courses_user_id" IMMEDIATE;
--
-- Create model UserProgress
--
CREATE TABLE "courses_userprogress" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "completed_lessons" integer NOT NULL, "quiz_scores" jsonb NOT NULL, "course_id" bigint NOT NULL, "user_id" bigint NOT NULL);
ALTER TABLE "courses_course" ADD CONSTRAINT "courses_course_category_id_d64b93bf_fk_courses_category_id" FOREIGN KEY ("category_id") REFERENCES "courses_category" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_course_category_id_d64b93bf" ON "courses_course" ("category_id");
ALTER TABLE "courses_lesson" ADD CONSTRAINT "courses_lesson_course_id_16bc4882_fk_courses_course_id" FOREIGN KEY ("course_id") REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_lesson_course_id_16bc4882" ON "courses_lesson" ("course_id");
ALTER TABLE "courses_quiz" ADD CONSTRAINT "courses_quiz_course_id_1a0543d1_fk_courses_course_id" FOREIGN KEY ("course_id") REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_quiz_course_id_1a0543d1" ON "courses_quiz" ("course_id");
ALTER TABLE "courses_quizquestion" ADD CONSTRAINT "courses_quizquestion_quiz_id_d8a2f3a5_fk_courses_quiz_id" FOREIGN KEY ("quiz_id") REFERENCES "courses_quiz" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_quizquestion_quiz_id_d8a2f3a5" ON "courses_quizquestion" ("quiz_id");
CREATE INDEX "courses_user_username_50bca808_like" ON "courses_user" ("username" varchar_pattern_ops);
ALTER TABLE "courses_user_groups" ADD CONSTRAINT "courses_user_groups_user_id_group_id_b5cd82da_uniq" UNIQUE ("user_id", "group_id");
ALTER TABLE "courses_user_groups" ADD CONSTRAINT "courses_user_groups_user_id_c63786e3_fk_courses_user_id" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "courses_user_groups" ADD CONSTRAINT "courses_user_groups_group_id_f1b5c084_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_user_groups_user_id_c63786e3" ON "courses_user_groups" ("user_id");
CREATE INDEX "courses_user_groups_group_id_f1b5c084" ON "courses_user_groups" ("group_id");
ALTER TABLE "courses_user_user_permissions" ADD CONSTRAINT "courses_user_user_permis_user_id_permission_id_e0e9296d_uniq" UNIQUE ("user_id", "permission_id");
ALTER TABLE "courses_user_user_permissions" ADD CONSTRAINT "courses_user_user_pe_user_id_699dc51a_fk_courses_u" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "courses_user_user_permissions" ADD CONSTRAINT "courses_user_user_pe_permission_id_5803efd0_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_user_user_permissions_user_id_699dc51a" ON "courses_user_user_permissions" ("user_id");
CREATE INDEX "courses_user_user_permissions_permission_id_5803efd0" ON "courses_user_user_permissions" ("permission_id");
ALTER TABLE "courses_review" ADD CONSTRAINT "courses_review_course_id_536a14f9_fk_courses_course_id" FOREIGN KEY ("course_id") REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "courses_review" ADD CONSTRAINT "courses_review_user_id_5a028109_fk_courses_user_id" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_review_course_id_536a14f9" ON "courses_review" ("course_id");
CREATE INDEX "courses_review_user_id_5a028109" ON "courses_review" ("user_id");
ALTER TABLE "courses_payment" ADD CONSTRAINT "courses_payment_user_id_4aaeee29_fk_courses_user_id" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_payment_user_id_4aaeee29" ON "courses_payment" ("user_id");
ALTER TABLE "courses_enrollment" ADD CONSTRAINT "courses_enrollment_course_id_2631503e_fk_courses_course_id" FOREIGN KEY ("course_id") REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "courses_enrollment" ADD CONSTRAINT "courses_enrollment_user_id_da3de16f_fk_courses_user_id" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_enrollment_course_id_2631503e" ON "courses_enrollment" ("course_id");
CREATE INDEX "courses_enrollment_user_id_da3de16f" ON "courses_enrollment" ("user_id");
CREATE INDEX "courses_course_instructor_id_5b0643dc" ON "courses_course" ("instructor_id");
ALTER TABLE "courses_userprogress" ADD CONSTRAINT "courses_userprogress_course_id_6a4e2ee3_fk_courses_course_id" FOREIGN KEY ("course_id") REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "courses_userprogress" ADD CONSTRAINT "courses_userprogress_user_id_b4dcd58f_fk_courses_user_id" FOREIGN KEY ("user_id") REFERENCES "courses_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "courses_userprogress_course_id_6a4e2ee3" ON "courses_userprogress" ("course_id");
CREATE INDEX "courses_userprogress_user_id_b4dcd58f" ON "courses_userprogress" ("user_id");
COMMIT;
BEGIN;
--
-- Change Meta options on userprogress
--
-- (no-op)
COMMIT;
BEGIN;
--
-- Change Meta options on userprogress
--
-- (no-op)
COMMIT;
