from rest_framework import filters, viewsets, serializers
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
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'email', 'message')


class RFPViewSet(viewsets.ModelViewSet):
    queryset = RequestForProposal.objects.all()
    serializer_class = RFPSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'email')

