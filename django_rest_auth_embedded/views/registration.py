from .base import BaseView

from ..serializers import RegistrationSerializer
from ..models import User


class RegistrationView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            return self.response_201(
                data={
                    'id': user.id,
                }
            )
        return self.response_400(data=serializer.errors)
