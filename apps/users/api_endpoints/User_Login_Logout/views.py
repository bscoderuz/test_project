from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            tokens = {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            return Response(tokens, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'detail': "Foydalanuvchi topilmadi yoki parol noto'g'ri"
                },
                status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        refresh = RefreshToken(request.auth)
        refresh.blacklist()
        return Response(
            {
                'detail': 'Successfully logged out.'
            }, status=status.HTTP_200_OK)


class BlacklistTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh = RefreshToken(request.auth)
        refresh.blacklist()

        return Response({'detail': 'Token added to blacklist.'}, status=status.HTTP_200_OK)


class RefreshTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            refresh = RefreshToken.for_user(request.user)
            access_token = str(refresh.access_token)
            return Response({'access': access_token}, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'detail': 'User not authenticated'
                }, status=status.HTTP_401_UNAUTHORIZED)


__all__ = ["UserLoginView", "UserLogoutView", "BlacklistTokenView", "RefreshTokenView"]
