from .models import Contact, Company
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(
        many=True, view_name='contact-detail', read_only=True)

    class Meta:
        model = Company
        fields = ['url', 'name', 'contacts']
