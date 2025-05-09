from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScanRequestSerializer
from core.application.use_cases import ScanUseCase
from core.infrastructure import ScannerService

class GoogleScanView(APIView):
    def post(self, request):
        serializer = ScanRequestSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            scan_use_case = ScanUseCase(ScannerService())
            result = scan_use_case.execute_google_scan(query)
            return Response({"result": result})
        return Response(serializer.errors, status=400)