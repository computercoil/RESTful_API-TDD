import unittest
import os
import json
from app import create_app, db

class BucketlistTestCase(unittest.TestCase):
    """ build up test case - tests - tear down test case"""
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.bucklist = {'name': 'This is a test'}
        
        with self.app.app_context()"
            # create all tables
            db.create_all()
            
    def test_bucklist_creation(self):
        """ Test POST request"""
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('test', str(res.data))
        
    def test_api_can_get_all_bucketlists(self):
        """ Test GET request"""
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/bucketlists/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('test', str(res.data))
        
    def test_api_can_get_bucketlist_by_id(self):
        """ Test API can get a bucketlist by id"""
        rv = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace(replace("'", "\""))
        result = self.client().get('/bucketlists/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('test', str(result.data))
        
    def test_bucketlist_can_be_edited(self):
        rv = self.client().post('/bucketlists/', data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put('/bucketlists/1', data={'name': 'Eat, pray and love again'})
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/bucketlists/1')
        self.assertIn('again',str(results.data))
        
    def test_bucketlist_deletion(self):
        """ Test DELETE """
        rv = self.client().post('/bucketlists/', data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/bucketlists/1')
        self.assertEqual(res.status_code, 200)
        result = self.client().get('/bucketlists/1')
        self.assertEqual(result.status_code, 404)
        
    def tearDown(self):
        """ tear down all test case"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
            
if __name__ == '__main__':
    unittest.main()