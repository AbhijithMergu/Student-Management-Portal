from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from onlineapp.models import College
import json


class CollegeTests(APITestCase):
	def test_add_college(self):
		url = reverse_lazy('onlineapp:api_colleges')
		data = {"name": "Karim College of engineering", "location": "Karimnagar", "acronym": "KCE", "contact": "contact@kce.edu"}
		count = College.objects.all().count()
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		url = 'http://127.0.0.1:8000/api/colleges/'
		response = self.client.get(url)
		response_data = json.loads(response.content)
		self.assertEqual(len(response_data),1)

	def test_detail_college(self):
		url = reverse_lazy('onlineapp:api_colleges')
		data = {"name": "Karim College of engineering", "location": "Karimnagar", "acronym": "KCE",
				"contact": "contact@kce.edu"}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		response_id = json.loads(response.content)['id']
		url = 'http://127.0.0.1:8000/api/colleges/'+str(response_id)+'/'
		response = self.client.get(url)
		self.assertEqual(response.status_code,status.HTTP_200_OK)
		print(response)
		response_data = json.loads(response.content)
		response_data.pop('id')
		self.assertEqual(response_data,data)

	def test_valid_update(self):
		url = reverse_lazy('onlineapp:api_colleges')
		data = {"name": "Karim College of engineering", "location": "Karimnagar", "acronym": "KCE",
				"contact": "contact@kce.edu"}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response_id = json.loads(response.content)['id']
		url = reverse_lazy('onlineapp:api_college_detail',kwargs={'pk':response_id})

		data = {'name':"Karim College of engineering", "location": "Karimnagar", "acronym": "KCP",
				"contact": "contact@kce.edu"}

		response = self.client.put(url,data)
		self.assertEqual(response.status_code,status.HTTP_200_OK)

	def test_invalid_update(self):
		url = reverse_lazy('onlineapp:api_colleges')
		data = {"name": "Karim College of engineering", "location": "Karimnagar", "acronym": "KCE",
				"contact": "contact@kce.edu"}
		response = self.client.post(url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response_id = json.loads(response.content)['id']
		url = reverse_lazy('onlineapp:api_college_detail', kwargs={'pk': response_id})

		data = {'name': "", "location": "Karimnagar", "acronym": "KCP",
				"contact": "contact@kce.edu"}

		response = self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	# def test_delete_college(self):
	# 	self.test_add_college()
	# 	url = 'http://127.0.0.1:8000/api/colleges/1'
	# 	response  = self.client.delete(url)
	# 	self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
	# 	self.assertEqual(College.obje)