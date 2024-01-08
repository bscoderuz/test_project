import logging
from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class TestAPIView(APIView):
    def get(self, request):
        try:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip is None:
                ip = request.META.get('REMOTE_ADDR')

            user_agent = request.META.get('HTTP_USER_AGENT')
            referer = request.META.get('HTTP_REFERER')

            log_data = f"{ip} - - [{self.get_current_time()}] \"GET {request.path} HTTP/1.1\" 200 {len(str(request.data))} \"{referer}\" \"{user_agent}\""
            logger.info(log_data)

            return Response(f"User IP: {ip}")

        except Exception as e:
            logger.error(f'Error: {str(e)}')
            data = {'error': 'Internal Server Error'}
            return Response(data, status=500)

    def get_current_time(self):
        return self.request.META.get('HTTP_X_REQUESTED_TIME', self.request.META.get('HTTP_X_DATE', ''))
