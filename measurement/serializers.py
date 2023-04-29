from rest_framework import serializers

from measurement.models import TempMeasurement, Sensor

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempMeasurement
        fields = ['sensor_id', 'temperature', 'date_measurement']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class DescriptionSensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']