import logging
from collections import Counter

from django.http import HttpResponse
from rest_framework.views import APIView

# Logger obyekti yaratish
logger = logging.getLogger(__name__)


class TestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Foydalanuvchi ma'lumotlari
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_agent = request.META.get('HTTP_USER_AGENT')
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

            # Loglarni yozish
            log_data = (
                f"User login - Username: {username}, Password: {password}, "
                f"IP: {ip_address}, User-Agent: {user_agent}"
            )

            # Eng ko'p yuborilgan so'rovlarni aniqlash
            most_common_requests = self.get_most_common_requests(request)

            # Eng ko'p uchraydigan server xatoliklarini aniqlash
            most_common_errors = self.get_most_common_errors(request)

            # Logdatani to'plash
            log_data += f"\nMost common requests: {most_common_requests}"
            log_data += f"\nMost common errors: {most_common_errors}"

            logger.info(log_data)

            # Bu joyda foydalanuvchini kirish vaqtida qanday ishlar bajariladi deb o'zingiz yozishingiz mumkin

            # Keyingi qadam (misol: foydalanuvchi kirish formasi ko'rsatish)
            return HttpResponse("Login success")

        except Exception as e:
            # Xatolarni loglarni yozish
            logger.error(f'Error during user login: {str(e)}')
            return HttpResponse("Internal Server Error", status=500)

    def get_most_common_requests(self, request):
        # Bu metodda eng ko'p yuborilgan so'rovlarni aniqlash uchun kerakli logika yoziladi
        # Misol uchun, request.path bilan so'rovlarni aniqlash mumkin
        # Sizning loyiha xususiyatlariga qarab, qanday logika qo'shib qo'yishingiz mumkin

        # Misol uchun, so'rovlarni yig'ib olish
        all_requests = [request.path for _ in range(10)]  # 10 marta takrorlanmoqda
        most_common_requests = Counter(all_requests).most_common(5)

        return most_common_requests

    def get_most_common_errors(self, request):
        # Bu metodda eng ko'p uchraydigan server xatoliklarini aniqlash uchun kerakli logika yoziladi
        # Sizning loyiha xususiyatlariga qarab, qanday logika qo'shib qo'yishingiz mumkin

        # Misol uchun, xatolarni yig'ib olish
        all_errors = ['500 Internal Server Error' for _ in range(5)]  # 5 marta takrorlanmoqda
        most_common_errors = Counter(all_errors).most_common(5)

        return most_common_errors
