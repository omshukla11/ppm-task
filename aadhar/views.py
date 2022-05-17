from .serializers import *
from rest_framework import (mixins, generics, status, permissions)
from django.http import Http404
from django.http.response import HttpResponse, JsonResponse

# Create your views here.

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            if request.user.is_admin:
                return True
            else:
                if request.user.is_staff and request.method=='GET':
                    return True
        return False


class AadharFilterAPI(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = AadharSerializer
    permission_classes = [CustomPermission]
    def get_queryset(self):
        try:
            if(self.kwargs['act']=='active'):
                print("active aadhar")
                return Aadhar.objects.filter(is_active=True)
            elif(self.kwargs['act']=='inactive'):
                print("inactive aadhar")
                return Aadhar.objects.filter(is_active=False)
        except:
            raise Http404
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

class AadharAPI(generics.ListCreateAPIView):
    serializer_class = AadharSerializer
    queryset = Aadhar.objects.all()
    permission_classes = [CustomPermission]


class AddressAPI(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [CustomPermission]

class AddressDetailAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = AddressSerializer
    permission_classes = [CustomPermission]
    queryset = Address.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    

class QualificationAPI(generics.ListCreateAPIView):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()
    permission_classes = [CustomPermission]

class QualificationDetailAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = QualificationSerializer
    permission_classes = [CustomPermission]
    queryset = Address.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class BankAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [CustomPermission]

class BankDetailAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = BankSerializer
    permission_classes = [CustomPermission]
    queryset = Address.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PerDetAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PersonalDetailsSerializer
    queryset = PersonalDetails.objects.all()
    permission_classes = [CustomPermission]

class PerDetAPIRUD(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = PersonalDetailsSerializer
    permission_classes = [CustomPermission]
    queryset = PersonalDetails.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AllInfoAPI(generics.ListAPIView):
    serializer_class = AllInfoSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        aadhar = Aadhar.objects.get(aadhar_no = self.kwargs['adh'])
        return AllInfo.objects.filter(aadhar = aadhar)