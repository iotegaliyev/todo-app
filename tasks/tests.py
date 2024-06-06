from users.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', first_name='First', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.task1 = Task.objects.create(title='Task 1', description='Description 1', status='new', user=self.user)
        self.task2 = Task.objects.create(title='Task 2', description='Description 2', status='in_progress',
                                         user=self.user)
        self.task3 = Task.objects.create(title='Task 3', description='Description 3', status='completed',
                                         user=self.user)

    def test_task_list(self):
        url = 'http://localhost:8000/api/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)

    def test_user_task_list(self):
        url = f'http://localhost:8000/api/users/{self.user.id}/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)

    def test_task_detail(self):
        url = f'http://localhost:8000/api/tasks/{self.task1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_task_complete(self):
        url = f'http://localhost:8000/api/tasks/{self.task1.id}/complete/'
        response = self.client.patch(url, data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'completed')

        updated_task = Task.objects.get(id=self.task1.id)
        self.assertEqual(updated_task.status, 'completed')

    def test_task_filter_by_status(self):
        url = 'http://localhost:8000/api/tasks/status/?status=new'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_task(self):
        url = 'http://localhost:8000/api/tasks/'
        data = {'title': 'New Task', 'description': 'Description of new task', 'status': 'new'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        new_task = Task.objects.get(title='New Task')
        self.assertEqual(new_task.description, 'Description of new task')

    def test_update_task(self):
        url = f'http://localhost:8000/api/tasks/{self.task2.id}/'
        data = {'title': 'Updated Task', 'description': 'Updated description', 'status': 'in_progress'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_task = Task.objects.get(id=self.task2.id)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.description, 'Updated description')

    def test_delete_task(self):
        url = f'http://localhost:8000/api/tasks/{self.task3.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task3.id)
