from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job, User
from .producer import publish
from .serializers import JobSerializer
import random


class JobViewSet(viewsets.ViewSet):
    def list(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('job_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        job = Job.objects.get(id=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def update(self, request, pk=None):
        job = Job.objects.get(id=pk)
        serializer = JobSerializer(instance=job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('job_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        job = Job.objects.get(id=pk)
        job.delete()
        publish('job_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })