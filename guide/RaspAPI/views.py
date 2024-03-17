from rest_framework.response import Response
from RaspAPI.rasp import rasp_grup
from RaspAPI.grup import rasp
from RaspAPI.save_grups import save_grups
from RaspAPI.save_rasp import save_rasp
from rest_framework.views import APIView
import json

class RaspGRUPAPIView(APIView):
    def get(self,request):
        grup = request.GET.get("grup")
        return Response(rasp_grup(grup))


class GRUPAPIView(APIView):
    def get(self,request):
        return Response(rasp())


class UpdateAPIView(APIView):
    def get(self,request):
        grup = save_grups()
        rasp = save_rasp()
        return Response(str({"Update_group" : grup ,"Update_rasp" : rasp}))