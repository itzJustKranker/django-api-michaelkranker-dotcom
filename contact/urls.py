from rest_framework import serializers, viewsets
from contact.models import Contact, RequestForProposal


class DefaultSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


class ContactSerializer(DefaultSerializers):
    class Meta:
        model = Contact
        fields = '__all__'


class RFPSerializer(DefaultSerializers):
    class Meta:
        model = RequestForProposal
        fields = '__all__'


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']


class RFPViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []

    queryset = RequestForProposal.objects.all()
    serializer_class = RFPSerializer
    http_method_names = ['post']

