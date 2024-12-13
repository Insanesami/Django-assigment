from myplatform.models import PlatformApiCall
from rest_framework.views import APIView

class PlatformApiMixin(APIView):
    def perform_platform_api_call(self, user, requested_url, requested_data, response_data):
        PlatformApiCall.objects.create(
            user=user,
            requested_url=requested_url,
            requested_data=requested_data,
            response_data=response_data,
        )
