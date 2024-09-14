# tests/utils/test_get_ip.py

from django.test import SimpleTestCase, RequestFactory
from django.utils.get_ip import get_ip

class GetIPTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_ip_direct(self):
        # Simulate a request with a direct IP address
        request = self.factory.get('/')
        request.META['REMOTE_ADDR'] = '192.168.1.1'
        ip = get_ip(request)
        self.assertEqual(ip, '192.168.1.1')

    def test_get_ip_forwarded(self):
        # Simulate a request with an IP address behind a proxy
        request = self.factory.get('/')
        request.META['HTTP_X_FORWARDED_FOR'] = '10.0.0.1, 192.168.1.1'
        ip = get_ip(request)
        self.assertEqual(ip, '10.0.0.1')
