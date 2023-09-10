from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.models import Task
from apis.serializers import TaskSerializer

class GetToDoAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        """
        description: API Endpoint for get all todo task
        return format: 
            [
                {
                    "id": id,
                    "title": "title",
                    "description": "description",
                    "date_created": "date time",
                    "complete": boolean
                }
            ]

        """
        try:
            all_tasks = Task.objects.all()
            all_test_serializer = TaskSerializer(all_tasks, many=True)
            return Response(all_test_serializer.data, status=status.HTTP_200_OK)

        except Exception as error:
            print(error)
            return Response({"msg": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateToDoAPIView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        """
        description: API Endpoint for create new todo task by following rules.

        rules:      - Payload data must be contained `title`, `description`, and `complete`.
                        - `title` in payload must be string (if not return bad request status).
                        - `description` in payload must be string (if not return bad request status).
                        - `complete` in payload must be boolean (if not return bad request status).

        """
        try:
            title = request.data.get("title", None)
            description = request.data.get("description", None)
            complete = request.data.get("complete", None)

            if not title or not description or not isinstance(complete, bool):
                return Response({"msg": "Data payload is not correct"}, status=status.HTTP_400_BAD_REQUEST)

            Task.objects.create(title=title, description=description, complete=complete)

            return Response({"msg": "Create task successful"}, status=status.HTTP_201_CREATED)

        except Exception as error:
            return Response({"msg": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditToDoAPIView(APIView):

    @staticmethod
    def put(request, *args, **kwargs):
        """
        description: API Endpoint for edit todo task.
        rules:      - Payload data must be contained `title`, `description`, and `complete`.
                        - `title` in payload must be string (if not return bad request status).
                        - `description` in payload must be string (if not return bad request status).
                        - `complete` in payload must be boolean (if not return bad request status).

        """
        try:
            task_id = kwargs.get("id", None)
            title = request.data.get("title", None)
            description = request.data.get("description", None)
            complete = request.data.get("complete", None)

            if not title or not description or not isinstance(complete, bool):
                return Response({"msg": "Data payload is not correct"}, status=status.HTTP_400_BAD_REQUEST)

            find_task = Task.objects.filter(id = task_id).first()
            if not find_task:
                return Response({"msg": "id is not correct"}, status=status.HTTP_400_BAD_REQUEST)
            
            find_task.title = title
            find_task.description = description
            find_task.complete = complete
            find_task.save()

            return Response({"msg": "Edit task successful"}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({"msg": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteToDoAPIView(APIView):  

    @staticmethod
    def delete(request, *args, **kwargs):
        """
        description: API Endpoint for delete todo task.

        """
        try:
            task_id = kwargs.get("id", None)
            find_task = Task.objects.filter(id = task_id).first()
            if not find_task:
                return Response({"msg": "id is not correct"}, status=status.HTTP_400_BAD_REQUEST)
            
            find_task.delete()
            return Response({"msg": "delete task successful"}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({"msg": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)