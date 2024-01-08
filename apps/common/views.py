from rest_framework.views import APIView
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


class TestAPIView(APIView):
    def get(self, request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip is None:
            ip = request.META.get('REMOTE_ADDR')

        try:
            logger.info('GET request received')
            return Response(f"User IP: {ip}")
        except Exception as e:
            logger.error(f'Error: {str(e)}')
            data = {'error': 'Internal Server Error'}
            return Response(data, status=500)
