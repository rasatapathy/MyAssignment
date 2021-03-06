# Generated by Django 4.0.4 on 2022-05-04 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=10)),
                ('phoneNumber', models.PositiveIntegerField()),
                ('designation', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'UserTable',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('projectTitle', models.CharField(max_length=10)),
                ('projectDescription', models.CharField(max_length=20)),
                ('projectCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LY3000.user')),
            ],
            options={
                'db_table': 'ProjectTable',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('issueID', models.AutoField(primary_key=True, serialize=False)),
                ('assigneeID', models.PositiveIntegerField()),
                ('reporterID', models.PositiveIntegerField()),
                ('issueName', models.CharField(max_length=20)),
                ('issueStatus', models.PositiveIntegerField()),
                ('issueType', models.IntegerField()),
                ('issueDescription', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LY3000.project')),
            ],
            options={
                'db_table': 'IssueTable',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.AutoField(primary_key=True, serialize=False)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LY3000.issue')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LY3000.user')),
                ('commentText', models.TextField()),
                ('createdOn', models.DateTimeField()),
                ('updatedOn', models.DateTimeField()),
                
            ],
            options={
                'db_table': 'CommentTable',
            },
        ),
    ]
