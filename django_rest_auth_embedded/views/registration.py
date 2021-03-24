from .base import BaseView

from ..serializers import RegistrationSerializer


class RegistrationView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return self.response_201(
                data={
                    'id': user.id,
                }
            )
        return self.response_400(data=serializer.errors)
