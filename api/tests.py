from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse


class BaseTest(APITestCase):
    """
    Class to set up test case
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.url_1  = "/api/locations?city=London&days=4"
        self.url_2  = "/api/locations?city=rrwtw&days=4"
        # self.api_urls = reverse("api_data")
        # self.api_urls_broken = reverse("api_data")
        return super().setUp()

    def get_data(self):
        """
            Get new data
        """
        return self.client.get(self.url_1)


    def get_data_broken(self):
        """
            Get new data
        """
        return self.client.get(self.url_2)

    def test_successful_get_data(self):
        """
        Test get data
        """
        response = self.get_data()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unsuccessful_get_data(self):
        """
        Test unsuccessful getting of data
        """
        response = self.get_data_broken()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)