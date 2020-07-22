from rest_framework.test import APITestCase
from rest_framework import status

class CustomTest(APITestCase) :

    def setUp(self) :
        #### Post the data and relationship using api
        self.client.post('address/', {'id':99999 ,'facility_address_one': 'Random address 1'} , format ='json')
        self.client.post('description/', {'id':99999 ,'short_description': 'RAND'} , format ='json')
        self.client.post('facility/', {'id':99999 ,'address_id':99999 , 'description_id':99999 , 'facility_id':99999} , format ='json')



    def test_get_facility(self) :
            #### Search using the short description
            response = self.client.get('facility?search=RAND')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(
                    (response.data['facility_id']),
                    (99999))





