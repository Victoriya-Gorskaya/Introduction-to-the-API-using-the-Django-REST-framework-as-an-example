from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, TempMeasurement
from measurement.serializers import MeasurementSerializer, DescriptionSensorSerializer, SensorSerializer


class CreateAPIView(ListAPIView):
    requests = Sensor.objects.all()
    serializers = DescriptionSensorSerializer

    def post(self, request):
        view_report = DescriptionSensorSerializer(data=request.data)
        if view_report.is_valid():
            view_report.save()
        return Response({'status': 'OK'})

class ListView(ListAPIView):
    requests = Sensor.objects.all()
    serializers = SensorSerializer

class RetrieveUpdateAPIView(RetrieveAPIView):
    requests = Sensor.objects.all()
    serializers = DescriptionSensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = DescriptionSensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ListCreateAPIView(ListAPIView):
    requests = TempMeasurement.objects.all()
    serializers = MeasurementSerializer

    def post(self, request):
        view_report = MeasurementSerializer(data=request.data)
        if view_report.is_valid():
            view_report.save()
        return Response({'status': 'OK'})