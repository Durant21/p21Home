import unittest
# import requests
# import responses
#
# from pyramid import testing
# from pyramid.view import view_config


# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#
#     def tearDown(self):
#         testing.tearDown()
#
#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'Home')
#
#
# class FunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from proto21_home import main
#         app = main({})
#         # from WebTest import TestApp
#         # self.testapp = TestApp(app)
#
#     def test_root(self):
#         res = self.testapp.get('/', status=200)
#         self.assertTrue(b'Pyramid' in res.body)


# class TutorialViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#
#     def tearDown(self):
#         testing.tearDown()
#
#     def test_hello_world(self):
#         from proto21_home.views.home_page import my_view3
#         import proto21_home.views.home_page
#         request = testing.DummyRequest()
#         response = my_view3(request)
#         # self.assertEqual(response.status_code, 200)
#         self.assertEqual( response['project'], 'iMii' )
#         # self.assertEqual( "a", search( new_URL ) )


# class TestCase( unittest.TestCase ):
#
#         @responses.activate
#         def test_Example(self):
#             responses.add( **{
#                 'method': responses.GET,
#                 'url': 'http://localhost:6543/api/people',
#                 'body': '{"error": "reason"}',
#                 'status': 404,
#                 'content_type': 'application/json',
#                 'adding_headers': {'X-Foo': 'Bar'}
#             } )
#
#             response = requests.get( 'http://localhost:6543/api/people' )
#
#             self.assertEqual( {'error': 'reason'}, response.json() )
#             self.assertEqual( 404, response.status_code )


class TestCase2( unittest.TestCase ):
    # @responses.activate
    def test_api_people(self):
        import requests

        url = "http://localhost:6543/api/people"

        headers = {
            'Accept': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "10acac8a-cfd7-4930-97cc-80518f469b07"
        }

        response = requests.request( "GET", url, headers=headers )

        # print(response.text())
        self.assertEqual( 200, response.status_code )


    def test_root(self):
        import requests

        url = "http://localhost:6543/"

        headers = {}

        response = requests.get(url)

        # print(response.text())
        self.assertEqual( 200, response.status_code )