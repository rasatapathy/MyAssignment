from rest_framework.response import Response
from rest_framework.decorators import api_view
from LY3000.models import Project, User, Issue, Comment
from .serializers import UserSerializer, ProjectSerializer, IssueSerializer, CommentSerializer


# ----------------------------USER--------------------------------------------------

@api_view(['GET'])
def getUserData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addUserData(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# ----------------------------PROJECT--------------------------------------------------

@api_view(['GET'])
def getProjectData(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addProjectData(request):
    serializer = ProjectSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
# -----------------------ISSUE-------------------------------------------------------

@api_view(['GET'])
def getIssueData(request):
    issues = User.objects.all()
    serializer = IssueSerializer(issues, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addIssueData(request):
    serializer = IssueSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# -----------------------Comment-------------------------------------------------------

@api_view(['GET'])
def getCommentData(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addCommentData(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
