
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import *
from django.contrib.auth import authenticate
from account.renderers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }
    
# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes=[userRenderer]
    def post(self, request, format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({ 'token':token,'messege':'Registration Successful'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status. HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer=UserLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print(email)
            print(password)
            user=authenticate(email=email, password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response({'token':token,'messege':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
       
# for detail about userprofile
class UserProfileView(APIView):
    renderer_classes= [userRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None): 
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [userRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangepasswordSerializer(data=request.data,
        context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
         return Response({'messege':'Password Changed Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status. HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    renderer_classes = [userRenderer]
    def post(self,request, format=None):
        serializer= SendPasswordResetEmilSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Reset link send.Please check your Email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status. HTTP_400_BAD_REQUEST)
    
class UserPasswordResetView(APIView):
    renderer_classes=[userRenderer]
    def post(self, request, uid, token, format=None):
        serializer= UserPasswordResetSerializer(data=request.data,
        context={'uid':'uid', 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status. HTTP_400_BAD_REQUEST)





class UserView(APIView):
    renderer_classes = [userRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)



