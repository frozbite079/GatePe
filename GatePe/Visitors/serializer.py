from rest_framework import serializers
from .models import *
from GatePeApp.serializer import *
class VisitorSerializer(serializers.ModelSerializer):
    # security_personnel= UserSerializer(many=True)
    # security_personnel= serializers.StringRelatedField(many=False)
    class Meta:
        model=Visitor
        fields=('name','contact','location','reason_for_visit','approval_status','visit_time','security_personnel')