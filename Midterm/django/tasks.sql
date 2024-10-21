BEGIN;
--
-- Create model Task
--
CREATE TABLE "tasks_task" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "completed" boolean NOT NULL);
COMMIT;