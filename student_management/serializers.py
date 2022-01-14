from rest_framework import serializers
from .models import StudentInfo,StudentAcademics

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model=StudentInfo
        fields=(
            'Roll_no',
            'Name',
            'Class',
            'School',
            'Mobile',
            'Address'
        )

class StudentAcademicsSerializer(serializers.ModelSerializer):
    class Meta:

        model:StudentAcademics
        fields=(
            'Maths',
            'Physics',
            'Chemistry',
            'Biology',
            'English'
        )