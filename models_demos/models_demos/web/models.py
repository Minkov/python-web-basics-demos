from enum import Enum

from django.db import models

# models.py

# Model fields == class attributes in Model classes


'''
PostgreSQL: varying char (30)
SQL Server: VARCHAR(30)
Other: CHARVAR(30) // only for demo

PostgreSQL: decimal
SQL Server: money
'''

'''
# First migration
CREATE TABLE "web_employee" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "first_name" varchar(30) NOT NULL,
    "years_of_experience" integer unsigned NOT NULL CHECK ("years_of_experience" >= 0),
    "review" text NOT NULL,
    "start_date" date NOT NULL,
    "email" varchar(254) NOT NULL,
    "created_on" datetime NOT NULL,
    "updated_on" datetime NOT NULL);
# Second migration
ALTER TABLE "web_employee" ADD COLUMN "last_name" varchar(40) NULL; 
CREATE TABLE "new__web_employee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "years_of_experience" integer unsigned NOT NULL CHECK ("years_of_experience" >= 0), "review" text NOT NULL, "start_date" date NOT NULL, "email" varchar(254) NOT NULL, "created_on" datetime NOT NULL, "updated_on" datetime NOT NULL, "last_name" varchar(40) NULL, "first_name" varchar(50) NOT NULL); (params None)
INSERT INTO "new__web_employee" ("id", "years_of_experience", "review", "start_date", "email", "created_on", "updated_on", "last_name", "first_name") SELECT "id", "years_of_experience", "review", "start_date", "email", "created_on", "updated_on", "last_name", "first_name" FROM "web_employee"; (params ())
DROP TABLE "web_employee"; (params ())
ALTER TABLE "new__web_employee" RENAME TO "web_employee"; (params ())
    
'''


# class EmployeeLevel(Enum):
#     JUNIOR = 'Junior',
#     REGULAR = 'Regular',
#     SENIOR = 'SENIOR'

class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    # Var char(50) => strings with max length 50
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    age = models.IntegerField(
        default=-7,
    )

    # int > 0
    years_of_experience = models.PositiveIntegerField()

    # Text => strings with unlimited length
    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(
        # Adds `UNIQUE` constraint
        unique=True,
        editable=False,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # This will be automatically set on creation (insert)
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be automatically set on each `save`/`update`
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )

    # One-to-many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        return f'Id: {self.pk}; Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


# Employee.objects.raw('SELECT * ')  # raw SQL
# Employee.objects.all()  # Select
# Employee.objects.create()  # Insert
# Employee.objects.filter()  # Select + Where
# Employee.objects.update()  # Update

'''
Django ORM (Object-relational mapping)
'''


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )
    # Additional info


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,  # Form validation
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )
