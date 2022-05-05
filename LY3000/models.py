from django.db import models
from django.forms import EmailField

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key = True)
    # Primary Key for the User Table, ID unique for every user
    pwd = models.CharField(max_length = 20)
    # password that needs to be checked during authentication
    name = models.CharField(max_length = 50)
    # Name of the user
    userName = models.CharField(max_length = 10)
    # userName used for login purposes
    phoneNumber = models.PositiveIntegerField()
    # contact Number of the User
    designation = models.CharField(max_length = 20)
    email = EmailField()

    class Meta:
        db_table = "UserTable"

class Project(models.Model):
    projectID = models.AutoField(primary_key = True)
    projectTitle = models.CharField(max_length = 10)
    projectDescription = models.CharField(max_length = 20)
    projectCreator = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = "ProjectTable"


class Issue(models.Model):
    issueID = models.AutoField(primary_key = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    assigneeID = models.PositiveIntegerField()
    reporterID = models.PositiveIntegerField()

    # assignee = models.CandidateKey(User, on_delete = models.CASCADE)
    # reporter = models.CandidateKey(User, on_delete = models.CASCADE)

    issueName = models.CharField(max_length=20)
    issueStatus = models.PositiveIntegerField()
    # 1. Open 2. In progress 3. In review 4. Code Complete 5. Done
    issueType = models.IntegerField()
    # 1: Bug 2: Task 3: Story 4: Epic
    issueDescription = models.CharField(max_length=50)

    class Meta:
        db_table = "IssueTable"
