from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_202_ACCEPTED,HTTP_406_NOT_ACCEPTABLE
from apps.core.serializers import *
from rest_framework.serializers import ValidationError
from routemobile.celery import app



class ItemsView(APIView):
    
    def post(self,request):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
            req_data = request.data
            serializer =  ItemsSerializer(data=req_data,partial=True)
            try :
                if serializer.is_valid(raise_exception=True) :
                    serializer.save()
                    d = app.send_task('tasks.updateItem', kwargs={"data":req_data})
                    response['result'] = "Item is under process!!"  
                    response['httpstatus'] = HTTP_202_ACCEPTED
                    return Response(data=response,status=response.get("httpstatus"))
                    
            except ValidationError as e:                
                error_detail = e.detail   
                error_messages = []
                for field, errors in error_detail.items():
                    error_messages.extend(errors)
                response["status"] = "error"
                response["httpstatus"] = HTTP_406_NOT_ACCEPTABLE
                response["reason"] = error_messages[0]
                return Response(data=response,status=response.get("httpstatus"))
                
            
        except Exception  as e :
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"ERROR DETAILS : {e}"
            
        return Response(data=response,status=response.get("httpstatus"))
        