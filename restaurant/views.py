from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .models import BookingModel,MenuModel
from .serializers import Bookingerializer,MenuSerializer,UserSerliazer
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

# Create your views here.
def test(request):
    return render(request,'index.html',{})

class MenuItemsView(generics.ListAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = []
    
class MenuItemsCreateView(generics.CreateAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminUser]
    
class SingleMenuItem(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminUser]

#class BookingView(APIView):
 #   def get(self,request):
  #      bookings = BookingModel.objects.all()
   #     serializer_class =Bookingerializer(bookings,many =True)
    #    return Response(serializer_class.data)
    
#class MenuView(APIView):
#    def post(self,request):
#        serializer = MenuSerializer(data = self.request.data)
#        if serializer.is_valid:
#            serializer.save()
#            return Response({"status":"success","data":serializer.data})
        
class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = Bookingerializer    
    permission_classes =[IsAuthenticatedOrReadOnly]
    
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerliazer
    permission_classes=[IsAdminUser]
    