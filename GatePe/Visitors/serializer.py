from rest_framework import serializers
from .models import *
from GatePeApp.serializer import *
class VisitorSerializer(serializers.ModelSerializer):
    # security_personnel=  ground_provider_profile_id=UserSerializer(many=False)
     # ground_provider_profile_id= serializers.StringRelatedField(many=False)
    class Meta:
        model=Visitor
        fields=('name','contact','location','reason_for_visit','approval_status','visit_time','security_personnel','resident')